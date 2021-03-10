# stdlib
import re
import sys
from typing import get_type_hints

# 3rd party
import packaging.requirements
import pytest
from coincidence import not_pypy, only_pypy

# this package
from seed_intersphinx_mapping import cache
from seed_intersphinx_mapping.core import get_sphinx_doc_url, search_dict


class TestSearchDict:

	example_dict = {
			"apple": "malus",
			"pear": "pyrus",
			"orange": "citrus",
			"grapefruit": "citrus",
			"lime": "citrus",
			"peach": "prunus",
			"plum": "prunus",
			"banana": "musa",
			"mango": "mangifera",
			"strawberry": "fragaria",
			"raspberry": "rubus",
			}

	@pytest.mark.parametrize(
			"regex, expects",
			[
					("pear", {"pear": "pyrus"}),
					("^pe", {"pear": "pyrus", "peach": "prunus"}),
					("grape", {"grapefruit": "citrus"}),
					("fruit", {}),
					(".*fruit$", {"grapefruit": "citrus"}),
					(re.compile("pear"), {"pear": "pyrus"}),
					(re.compile("^pe"), {"pear": "pyrus", "peach": "prunus"}),
					(re.compile("grape"), {"grapefruit": "citrus"}),
					(re.compile("fruit"), {}),
					(re.compile(".*fruit$"), {"grapefruit": "citrus"}),
					]
			)
	def test_success(self, regex, expects):
		assert search_dict(self.example_dict, regex) == expects

	@pytest.mark.parametrize(
			"dictionary, expects, match",
			[
					("abc", AttributeError, ".* object has no attribute 'items'"),
					(1234, AttributeError, ".* object has no attribute 'items'"),
					(12.34, AttributeError, ".* object has no attribute 'items'"),
					([12.34, "abc", 1234], AttributeError, ".* object has no attribute 'items'"),
					((12.34, "abc", 1234), AttributeError, ".* object has no attribute 'items'"),
					({12.34, "abc", 1234}, AttributeError, ".* object has no attribute 'items'"),
					pytest.param(
							{12.34: "abc"},
							TypeError,
							"expected string or bytes-like object",
							marks=not_pypy("Error message differs on PyPy"),
							),
					pytest.param(
							{12.34: "abc"},
							TypeError,
							"can't use a string pattern on a bytes-like object",
							marks=only_pypy("Error message differs on PyPy"),
							),
					]
			)
	def test_errors_dict(self, dictionary, expects, match):
		with pytest.raises(expects, match=match):
			search_dict(dictionary, '')

	@pytest.mark.parametrize(
			"regex, expects, match",
			[
					(1234, TypeError, "first argument must be string or compiled pattern"),
					(12.34, TypeError, "first argument must be string or compiled pattern"),
					([12.34, "abc", 1234], TypeError, "unhashable type: 'list'"),
					((12.34, "abc", 1234), TypeError, "first argument must be string or compiled pattern"),
					({12.34, "abc", 1234}, TypeError, "unhashable type: 'set'"),
					({12.34: "abc"}, TypeError, "unhashable type: 'dict'"),
					]
			)
	def test_errors_regex(self, regex, expects, match):
		with pytest.raises(expects, match=match):
			search_dict(self.example_dict, regex)


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
