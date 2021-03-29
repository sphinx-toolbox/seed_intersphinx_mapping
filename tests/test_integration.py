# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus


@pytest.fixture()
def requirements(tmp_pathplus):
	fake_repo_root = tmp_pathplus.parent

	(fake_repo_root / "requirements.txt").write_text("""\
domdf_python_tools
packaging
requests
pandas
appdirs
""")


def test_integration(requirements, the_app):
	# app is a Sphinx application object for default sphinx project (`tests/doc-test/test-root`).
	the_app.build()

	domdf_python_tools_url = "https://domdf-python-tools.readthedocs.io/en/latest/"

	assert the_app.env.config.intersphinx_mapping == {
			"domdf-python-tools": ("domdf-python-tools", (domdf_python_tools_url, (None, ))),
			"packaging": ("packaging", ("https://packaging.pypa.io/en/latest/", (None, ))),
			"requests": ("requests", ("https://docs.python-requests.org/en/master/", (None, ))),
			"pandas": ("pandas", ("https://pandas.pydata.org/pandas-docs/stable/", (None, ))),
			}
	assert the_app.env.config.pkg_requirements_source == "requirements"
	assert the_app.env.config.repository_root == str(PathPlus(the_app.srcdir).parent)
