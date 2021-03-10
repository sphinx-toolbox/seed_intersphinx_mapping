# stdlib
import sys
from typing import get_type_hints

# 3rd party
import packaging.requirements
import pytest

# this package
from seed_intersphinx_mapping import cache
from seed_intersphinx_mapping.core import get_sphinx_doc_url, search_dict


def test_get_sphinx_doc_url():
	assert cache.clear(get_sphinx_doc_url)

	assert get_sphinx_doc_url("domdf_python_tools") == "https://domdf-python-tools.readthedocs.io/en/latest/"
	assert get_sphinx_doc_url("domdf-python-tools") == "https://domdf-python-tools.readthedocs.io/en/latest/"

	with pytest.raises(packaging.requirements.InvalidRequirement, match="No such project 'domdf_python_toolsz'"):
		get_sphinx_doc_url("domdf_python_toolsz")

	with pytest.raises(ValueError, match="Documentation URL not found in data from PyPI."):
		get_sphinx_doc_url("slumber")

	with pytest.raises(ValueError, match="objects.inv not found at url."):
		get_sphinx_doc_url("isort")

	assert cache.clear(get_sphinx_doc_url)
	assert not (cache.cache_dir / "get_sphinx_doc_url.json").is_file()

	with pytest.raises(ValueError, match="Documentation URL not found in data from PyPI."):
		get_sphinx_doc_url("sphinx-prompt")


def test_get_sphinx_doc_url_wrapping():
	assert get_sphinx_doc_url.__name__ == "get_sphinx_doc_url"

	if sys.version_info >= (3, 10):
		assert get_sphinx_doc_url.__annotations__ == {"pypi_name": "str", "return": "str"}
	else:
		assert get_sphinx_doc_url.__annotations__ == {"pypi_name": str, "return": str}

	assert get_type_hints(get_sphinx_doc_url) == {"pypi_name": str, "return": str}

	assert get_sphinx_doc_url.__defaults__ is None
	assert get_sphinx_doc_url.__doc__.startswith("\n	Returns the URL to the given project's Sphinx documentation.")
	assert get_sphinx_doc_url.__wrapped__
