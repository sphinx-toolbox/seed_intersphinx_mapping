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
import re
from typing import Dict, Optional, Tuple, Union

# 3rd party
import dist_meta
import requests
from apeye.requests_url import RequestsURL
from dist_meta.metadata_mapping import MetadataMapping
from domdf_python_tools.compat import importlib_resources
from domdf_python_tools.utils import stderr_writer
from packaging.requirements import Requirement
from pypi_json import PyPIJSON

# this package
from seed_intersphinx_mapping.cache import cache
from seed_intersphinx_mapping.extension import setup

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "1.0.1"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["get_sphinx_doc_url", "fallback_mapping", "seed_intersphinx_mapping"]

_DOCUMENTATION_RE = re.compile(r"^[dD]oc(s|umentation)")


def _get_project_links(project_name: str) -> MetadataMapping:
	"""
	Returns the web links for the given project.

	The exact keys vary, but common keys include "Documentation" and "Issue Tracker".

	:param project_name:
	"""

	urls = MetadataMapping()

	# Try a local package first
	try:
		dist = dist_meta.distributions.get_distribution(project_name)
		raw_urls = dist.get_metadata().get_all("Project-URL", default=())

		for url in raw_urls:
			label, url, *_ = map(str.strip, url.split(','))
			if _DOCUMENTATION_RE.match(label):
				urls[label] = url

	except dist_meta.distributions.DistributionNotFoundError:
		# Fall back to PyPI

		with PyPIJSON() as client:
			metadata = client.get_metadata(project_name).info

		if "project_urls" in metadata and metadata["project_urls"]:
			for label, url in metadata["project_urls"].items():
				if _DOCUMENTATION_RE.match(label):
					urls[label] = url

	return urls


@cache
def get_sphinx_doc_url(pypi_name: str) -> str:
	"""
	Returns the URL to the given project's Sphinx documentation.

	Not all projects include this URL in their distributions
	and therefore it may not be possible to determine it from PyPI.

	Responses are cached to prevent overloading the PyPI server.
	The cache can be cleared as follows:

	.. prompt:: bash

		python3 -m seed_intersphinx_mapping

	.. latex:vspace:: -10px

	:param pypi_name: The name of the project on PyPI

	:returns: The URL of the project's Sphinx documentation.

	:raises:

		* :exc:`ValueError` if the url could not be determined.
		* :exc:`packaging.requirements.InvalidRequirement` if the project could not be found on PyPI.

	.. versionchanged:: 0.4.0

		Now raises :exc:`~packaging.requirements.InvalidRequirement` rather than
		:exc:`apeye.slumber_url.exceptions.HttpNotFoundError` if the project could not be found on PyPI.
	"""

	for key, value in _get_project_links(pypi_name).items():

		# Follow redirects to get actual URL
		r = RequestsURL(value).head(allow_redirects=True, timeout=10)
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
