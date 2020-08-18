#!/usr/bin/env python3
#
#  cache.py
"""
Caching functions.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import inspect
import json
import shutil
import warnings
from functools import wraps
from typing import Any, Callable, Dict, Iterable, Optional, Union

# 3rd party
from appdirs import user_cache_dir
from domdf_python_tools.paths import PathPlus


def posargs2kwargs(
		args: Iterable[Any],
		posarg_names: Union[Iterable[str], Callable],
		kwargs: Optional[Dict[str, Any]] = None,
		) -> Dict[str, Any]:
	"""
	Convert the positional args in ``args`` to kwargs, based on the relative order of ``args`` and ``posarg_names``.

	:param args: List of positional arguments provided to a function.
	:param posarg_names: Either a list of positional argument names for the function, or the function object.
	:param kwargs: Optional mapping of keyword argument names to values.
		The arguments will be added to this dictionary if provided.
	:default kwargs: ``{}``

	:return:
	"""

	if kwargs is None:
		kwargs = {}

	if callable(posarg_names):
		posarg_names = inspect.getfullargspec(posarg_names).args

	kwargs.update(zip(posarg_names, args))

	return kwargs


class Cache:

	def __init__(self, app_name: str):
		self.app_name: str = str(app_name)
		self.cache_dir = PathPlus(user_cache_dir(f"{self.app_name}_cache"))
		self.cache_dir.maybe_make(parents=True)

		# Mapping of function names to their caches
		self.caches: Dict[str, Dict[str, Any]] = {}

	def clear(self, func: Optional[Callable] = None) -> bool:
		"""
		Clear the cache.

		:param func: Optional function to clear the cache for.
			By default, the whole cache is cleared.
		:no-default func:

		:returns: True to indicate success. False otherwise.
		"""

		try:
			if func is None:
				shutil.rmtree(self.cache_dir)
				self.cache_dir.maybe_make()
				for function in self.caches:
					del self.caches[function]
					self.caches[function] = {}
			else:
				function_name = func.__name__
				cache_file = self.cache_dir / f"{function_name}.json"
				if cache_file.is_file():
					cache_file.unlink()

				if function_name in self.caches:
					del self.caches[function_name]
				self.caches[function_name] = {}

			return True

		except Exception as e:  # pragma: no cover
			warnings.warn(f"Could not remove cache. The error was: {e}")
			return False

	def load_cache(self, func: Callable) -> None:
		"""
		Loads the cache for the given function

		:param func:
		"""

		cache_file: PathPlus = self.cache_dir / f"{func.__name__}.json"

		if cache_file.is_file():
			cache = json.loads(cache_file.read_text())
		else:
			cache = {}

		self.caches[func.__name__] = cache
		return cache

	def __call__(self, func: Callable):
		"""
		Decorator to cache the return values of a function based on its inputs.

		:param func:
		"""

		function_name = func.__name__
		posargs: Iterable[str] = inspect.getfullargspec(func).args
		cache_file: PathPlus = self.cache_dir / f"{function_name}.json"
		self.load_cache(func)

		@wraps(func)
		def wrapper(*args, **kwargs):
			kwargs: Dict[str, Any] = posargs2kwargs(args, posargs, kwargs)  # type: ignore
			key: str = json.dumps(kwargs)
			response: Any

			cache = self.caches[function_name]
			if key in cache:
				# Return cached response
				response = json.loads(cache[key])
			else:
				response = func(**kwargs)

				if response is not None:
					# Don't cache None values.
					cache[key] = json.dumps(response)

			cache_file.write_text(json.dumps(cache))

			return response

		return wrapper


cache = Cache("seed_intersphinx_mapping")
