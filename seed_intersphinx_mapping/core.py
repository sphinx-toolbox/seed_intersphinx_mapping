#!/usr/bin/env python3
#
#  core.py
"""
Core functionality.
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
import functools
import json
import re
import warnings
from typing import Any, Dict, Optional, Pattern, Tuple, Union

# 3rd party
import importlib_resources
import requests
from apeye.url import SlumberURL
from domdf_python_tools.typing import PathLike

# this package
from seed_intersphinx_mapping.cache import cache
from seed_intersphinx_mapping.requirements_parsers import parse_requirements_txt

__all__ = ["search_dict", "get_sphinx_doc_url", "fallback_mapping", "seed_intersphinx_mapping", "pypi_api"]

#: Instance of :class:`apeye.url.SlumberURL` for the PyPI REST API endpoint.
pypi_api = SlumberURL("https://pypi.org/pypi/")


def search_dict(dictionary: Dict[str, Any], regex: Union[str, Pattern]) -> Dict[str, Any]:
	"""
	Return the subset of the dictionary whose keys match the regex.

	:param dictionary:
	:param regex:
	"""

	if not isinstance(regex, Pattern):
		regex = re.compile(regex)

	return {key: value for key, value in dictionary.items() if regex.match(key)}


@cache
def get_sphinx_doc_url(pypi_name: str) -> str:
	"""
	Returns the URl to the given project's Sphinx documentation.

	Not all projects include this URl in their distributions and therefore it may not be possible to determine it from PyPI.

	Responses are cached to prevent overloading the PyPI server.
	If using the Sphinx extension the cache is cleared whenever a document is rebuilt.
	It can also be cleared manually as follows:

	.. code-block:: python

		>>> from seed_intersphinx_mapping import cache, get_sphinx_doc_url
		>>> cache.clear(get_sphinx_doc_url)
		True

	:param pypi_name: The name of the project on PyPI

	:return: The URl of the project's Sphinx documentation.

	:raises: | :exc:`ValueError` if the url could not be determined.
		| :exc:`slumber.exceptions.HttpNotFoundError` if the project could not be found on PyPI.
	"""

	pypi_data = (pypi_api / pypi_name / "json").get()

	if "project_urls" in pypi_data["info"] and pypi_data["info"]["project_urls"]:
		docs_dict = search_dict(pypi_data["info"]["project_urls"], r"^[dD]oc(s|umentation)")
		if docs_dict:

			# Follow redirects to get actual URL
			r = requests.head(list(docs_dict.values())[0], allow_redirects=True)
			if r.status_code != 200:  # pragma: no cover
				raise ValueError("Documentation URl not found.")

			docs_url = r.url

			if docs_url.endswith("/"):
				objects_inv_url = f"{docs_url}objects.inv"
			else:  # pragma: no cover
				objects_inv_url = f"{docs_url}/objects.inv"

			r = requests.head(objects_inv_url)
			if r.status_code != 200:
				raise ValueError("objects.inv not found at url.")

			return docs_url

	raise ValueError("Documentation URl not found in data from PyPI.")


@functools.lru_cache()
def fallback_mapping() -> Dict[str, str]:
	"""
	Returns the fallback mapping for projects that do not provide a link to their documentation on PyPI.

	The mapping is loaded from JSON data on demand, and consists of ``project_name: url`` pairs.
	"""
	# this package
	import seed_intersphinx_mapping
	with importlib_resources.path(seed_intersphinx_mapping, "fallback_mapping.json") as path:
		with open(path, encoding="UTF-8") as fp:
			return json.load(fp)


def seed_intersphinx_mapping(base_dir: PathLike) -> Dict[str, Tuple[str, Optional[str]]]:
	"""
	Returns an intersphinx mapping dictionary for the projects listed in the ``requirements.txt`` file.

	:param base_dir: The directory in which to find the ``requirements.txt`` file.
	"""

	intersphinx_mapping: Dict[str, Tuple[str, Optional[str]]] = {}

	for project_name in parse_requirements_txt(base_dir):
		try:
			doc_url = get_sphinx_doc_url(project_name)
			intersphinx_mapping[project_name] = (doc_url, None)
		except (ValueError, requests.exceptions.ConnectionError):
			# Couldn't get it from PyPI, trying fallback mapping
			if project_name in fallback_mapping():
				doc_url = fallback_mapping()[project_name]
				intersphinx_mapping[project_name] = (doc_url, None)
			else:
				warnings.warn(f"Unable to determine documentation url for project {project_name}")

	return intersphinx_mapping
