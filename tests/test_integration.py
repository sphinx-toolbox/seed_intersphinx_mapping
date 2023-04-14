# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus


@pytest.fixture()
def requirements(tmp_pathplus: PathPlus) -> None:
	fake_repo_root = tmp_pathplus.parent

	(fake_repo_root / "requirements.txt").write_text("""\
domdf_python_tools
packaging
requests
pandas
appdirs
""")


@pytest.mark.usefixtures("requirements")
def test_integration(the_app):
	# app is a Sphinx application object for default sphinx project (`tests/doc-test/test-root`).
	the_app.build()

	domdf_python_tools_url = "https://domdf-python-tools.readthedocs.io/en/latest/"

	assert the_app.env.config.intersphinx_mapping == {
			"domdf-python-tools": ("domdf-python-tools", (domdf_python_tools_url, (None, ))),
			"packaging": ("packaging", ("https://packaging.pypa.io/en/stable/", (None, ))),
			"requests": ("requests", ("https://requests.readthedocs.io/en/latest/", (None, ))),
			"pandas": ("pandas", ("https://pandas.pydata.org/docs/", (None, ))),
			}
	assert the_app.env.config.pkg_requirements_source == "requirements"
	assert the_app.env.config.repository_root == str(PathPlus(the_app.srcdir).parent)
