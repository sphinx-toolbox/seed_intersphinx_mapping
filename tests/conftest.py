# stdlib
import pathlib
import sys

# 3rd party
import pytest
from sphinx.testing.path import path

if sys.version_info >= (3, 10):
	# stdlib
	import types
	types.Union = types.UnionType

pytest_plugins = ("sphinx.testing.fixtures", "coincidence")


@pytest.fixture(scope="session")
def rootdir():
	rdir = pathlib.Path(__file__).parent.absolute() / "doc-test"
	if not (rdir / "test-root").is_dir():
		(rdir / "test-root").mkdir(parents=True)
	return path(rdir)


@pytest.fixture()
def the_app(app):
	return app
