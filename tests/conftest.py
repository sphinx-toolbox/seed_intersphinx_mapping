# stdlib
import pathlib

# 3rd party
import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
	rdir = pathlib.Path(__file__).parent.absolute() / "doc-test"
	if not (rdir / "test-root").is_dir():
		(rdir / "test-root").mkdir(parents=True)
	return path(rdir)


@pytest.fixture()
def the_app(app):
	return app
