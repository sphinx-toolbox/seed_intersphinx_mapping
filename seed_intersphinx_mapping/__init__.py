#!/usr/bin/env python3
#
#  __init__.py
"""
Populate the Sphinx 'intersphinx_mapping' dictionary from the project's requirements.

.. versionchanged:: 0.5.0

	The functions formerly in ``seed_intersphinx_mapping.core`` can now be found here.
"""
#
#  Copyright © 2020-2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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
from typing import Dict, Optional, Tuple, Union

# 3rd party
import requests
from cawdrey.utils import search_dict
from domdf_python_tools.compat import importlib_resources
from domdf_python_tools.utils import stderr_writer
from packaging.requirements import Requirement
from shippinglabel import get_project_links

# this package
from seed_intersphinx_mapping.cache import cache
from seed_intersphinx_mapping.extension import setup

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.5.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["get_sphinx_doc_url", "fallback_mapping", "seed_intersphinx_mapping"]


@cache
def get_sphinx_doc_url(pypi_name: str) -> str:
	"""
	Returns the URL to the given project's Sphinx documentation.

	Not all projects include this URL in their distributions and therefore it may not be possible to determine it from PyPI.

	Responses are cached to prevent overloading the PyPI server.
	The cache can be cleared as follows:

	.. prompt:: bash

		python3 -m seed_intersphinx_mapping

	.. TODO:: automatic cache clearing, perhaps using ``intersphinx_cache_limit``

	:param pypi_name: The name of the project on PyPI

	:returns: The URL of the project's Sphinx documentation.

	:raises: | :exc:`ValueError` if the url could not be determined.
		| :exc:`packaging.requirements.InvalidRequirement` if the project could not be found on PyPI.

	.. versionchanged:: 0.4.0

		Now raises a :exc:`packaging.requirements.InvalidRequirement` rather than a
		:exc:`apeye.slumber_url.exceptions.HttpNotFoundError` if the project could not be found on PyPI.
	"""

	docs_dict = search_dict(get_project_links(pypi_name), r"^[dD]oc(s|umentation)")

	if docs_dict:

		# Follow redirects to get actual URL
		r = requests.head(list(docs_dict.values())[0], allow_redirects=True, timeout=10)
		if r.status_code != 200:  # pragma: no cover
			raise ValueError(f"Documentation URL not found: HTTP Status {r.status_code}.")

		docs_url = r.url

		if docs_url.endswith('/'):
			objects_inv_url = f"{docs_url}objects.inv"
		else:  # pragma: no cover
			objects_inv_url = f"{docs_url}/objects.inv"

		r = requests.head(objects_inv_url)
		if r.status_code != 200:
			raise ValueError(f"objects.inv not found at url {objects_inv_url}: HTTP Status {r.status_code}.")

		return docs_url

	raise ValueError("Documentation URL not found in data from PyPI.")


@functools.lru_cache()
def fallback_mapping() -> Dict[str, str]:
	"""
	Returns the fallback mapping for projects that do not provide a link to their documentation on PyPI.

	The mapping is loaded from JSON data on demand, and consists of ``project_name: url`` pairs.
	"""

	return json.loads(importlib_resources.read_text("seed_intersphinx_mapping", "fallback_mapping.json"))


def seed_intersphinx_mapping(*requirements: Union[Requirement, str]) -> Dict[str, Tuple[str, Optional[str]]]:
	r"""
	Returns an intersphinx mapping dictionary for the project's requirements.

	:param \*requirements: The requirements to find the documentation for.

	.. versionchanged:: 0.4.0

		Now takes the requirements as arguments rather than
		a directory to read the ``requirements.txt`` file from.
	"""

	intersphinx_mapping: Dict[str, Tuple[str, Optional[str]]] = {}

	for requirement in requirements:
		if isinstance(requirement, Requirement):
			project_name = requirement.name
		else:
			project_name = str(requirement)

		try:
			doc_url = get_sphinx_doc_url(project_name)
			intersphinx_mapping[project_name] = (doc_url, None)
		except (ValueError, requests.exceptions.ConnectionError, requests.exceptions.Timeout):
			# Couldn't get it from PyPI, trying fallback mapping
			if project_name in fallback_mapping():
				doc_url = fallback_mapping()[project_name]
				intersphinx_mapping[project_name] = (doc_url, None)
			else:
				stderr_writer(f"WARNING: Unable to determine documentation url for project {project_name}")

	return intersphinx_mapping
