# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus


@pytest.fixture()
def requirements(tmp_path):
	fake_repo_root = PathPlus(tmp_path).parent

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
	assert the_app.env.config.intersphinx_mapping == {
			"domdf_python_tools":
					("domdf_python_tools", ("https://domdf-python-tools.readthedocs.io/en/latest/", (None, ))),
			'packaging': ('packaging', ('https://packaging.pypa.io/en/latest/', (None, ))),
			"requests": ("requests", ("https://requests.readthedocs.io/en/master/", (None, ))),
			"pandas": ("pandas", ("https://pandas.pydata.org/pandas-docs/stable/", (None, ))),
			}
	assert the_app.env.config.pkg_requirements_source == "requirements"
	assert the_app.env.config.repository_root == str(PathPlus(the_app.srcdir).parent)
