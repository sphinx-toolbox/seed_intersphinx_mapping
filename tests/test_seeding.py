# stdlib
from types import SimpleNamespace

# 3rd party
import pytest
import toml
from coincidence import AdvancedDataRegressionFixture
from shippinglabel.requirements import read_requirements

# this package
from seed_intersphinx_mapping import seed_intersphinx_mapping
from seed_intersphinx_mapping.extension import sphinx_seed_intersphinx_mapping
from seed_intersphinx_mapping.requirements_parsers import (
		parse_flit_requirements,
		parse_pyproject_toml,
		parse_requirements_txt
		)
from tests.test_requirements_parsers import bad_example_requirements, example_requirements_a

expected_mapping_a = {
		"domdf-python-tools": ("https://domdf-python-tools.readthedocs.io/en/latest/", None),
		"packaging": ("https://packaging.pypa.io/en/latest/", None),
		"requests": ("https://docs.python-requests.org/en/master/", None),
		"slumber": ("https://slumber.readthedocs.io/en/v0.6.0/", None),
		"sphinx": ("https://www.sphinx-doc.org/en/3.x/", None),
		}
bad_expected_mapping = {
		"domdf-python-tools": ("https://domdf-python-tools.readthedocs.io/en/latest/", None),
		"packaging": ("https://packaging.pypa.io/en/latest/", None),
		"sphinx": ("https://www.sphinx-doc.org/en/3.x/", None),
		}


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_mapping_a),
				(bad_example_requirements, bad_expected_mapping),
				]
		)
def test_seed_intersphinx_mapping(tmp_pathplus, contents, expects, capsys):
	(tmp_pathplus / "requirements.txt").write_text(contents)

	assert seed_intersphinx_mapping(*parse_requirements_txt(tmp_pathplus)) == expects
	err = capsys.readouterr().err
	assert err == "WARNING: Unable to determine documentation url for project sphinxcontrib-domaintools\n"

	requirements, comments, invalid = read_requirements(tmp_pathplus / "requirements.txt", include_invalid=True)
	assert seed_intersphinx_mapping(*requirements) == expects
	err = capsys.readouterr().err
	assert err == "WARNING: Unable to determine documentation url for project sphinxcontrib-domaintools\n"


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_mapping_a),
				(bad_example_requirements, bad_expected_mapping),
				]
		)
def test_seed_intersphinx_mapping_pyproject(tmp_pathplus, contents, expects, capsys):
	data = {"project": {"dependencies": contents.splitlines()}}
	(tmp_pathplus / "pyproject.toml").write_clean(toml.dumps(data))

	assert seed_intersphinx_mapping(*parse_pyproject_toml(tmp_pathplus)) == expects
	err = capsys.readouterr().err
	assert err == "WARNING: Unable to determine documentation url for project sphinxcontrib-domaintools\n"


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_mapping_a),
				(bad_example_requirements, bad_expected_mapping),
				]
		)
def test_seed_intersphinx_mapping_flit(tmp_pathplus, contents, expects, capsys):
	data = {"tool": {"flit": {"metadata": {"requires": contents.splitlines()}}}}
	(tmp_pathplus / "pyproject.toml").write_clean(toml.dumps(data))

	assert seed_intersphinx_mapping(*parse_flit_requirements(tmp_pathplus)) == expects
	err = capsys.readouterr().err
	assert err == "WARNING: Unable to determine documentation url for project sphinxcontrib-domaintools\n"


@pytest.mark.parametrize("pkg_requirements_source", ["requirements", "flit", "pyproject", "pyproject.toml"])
@pytest.mark.parametrize(
		"contents",
		[
				pytest.param(example_requirements_a, id="example_requirements_a"),
				pytest.param(bad_example_requirements, id="bad_example_requirements"),
				]
		)
def test_sphinx_seed_intersphinx_mapping_mocked(
		tmp_pathplus,
		capsys,
		contents,
		advanced_data_regression: AdvancedDataRegressionFixture,
		pkg_requirements_source: str
		):

	data = {
			"project": {"dependencies": contents.splitlines()},
			"tool": {"flit": {"metadata": {"requires": contents.splitlines()}}}
			}

	(tmp_pathplus / "pyproject.toml").write_clean(toml.dumps(data))
	(tmp_pathplus / "requirements.txt").write_text(contents)

	app = SimpleNamespace()
	app.srcdir = tmp_pathplus

	config = SimpleNamespace()
	config.intersphinx_mapping = {}
	config.pkg_requirements_source = pkg_requirements_source
	config.repository_root = '.'

	sphinx_seed_intersphinx_mapping(app, config)  # type: ignore

	advanced_data_regression.check(config.intersphinx_mapping)

	err = capsys.readouterr().err
	assert err == "WARNING: Unable to determine documentation url for project sphinxcontrib-domaintools\n"


def test_sphinx_seed_intersphinx_mapping_list_mocked(
		tmp_pathplus,
		advanced_data_regression: AdvancedDataRegressionFixture,
		):

	my_project = tmp_pathplus / "my_project"

	for submodule in ["foo", "bar", "baz"]:
		(my_project / submodule).mkdir(parents=True)

	(my_project / "foo" / "requirements.txt").write_lines(["domdf_python_tools>=0.4.8", "packaging>=20.4"])
	(my_project / "bar" / "requirements.txt").write_lines(["requests>=2.24.0", "slumber>=0.7.1"])
	(my_project / "baz" / "requirements.txt").write_lines(["sphinx>=3.0.3"])

	app = SimpleNamespace()
	app.srcdir = tmp_pathplus

	config = SimpleNamespace()
	config.intersphinx_mapping = {}
	config.pkg_requirements_source = [
			"my_project/foo",
			"my_project/bar",
			"my_project/baz",
			]
	config.repository_root = '.'

	sphinx_seed_intersphinx_mapping(app, config)  # type: ignore

	advanced_data_regression.check(config.intersphinx_mapping)
