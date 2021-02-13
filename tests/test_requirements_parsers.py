# 3rd party
import pytest
import toml

# this package
from seed_intersphinx_mapping.requirements_parsers import (
		parse_flit_requirements,
		parse_pyproject_toml,
		parse_requirements_txt
		)

example_requirements_a = """\
domdf_python_tools>=0.4.8
packaging>=20.4
requests>=2.24.0
slumber>=0.7.1
sphinx>=3.0.3
sphinxcontrib-domaintools==0.3
"""

expected_requirements_a = [
		"domdf-python-tools",
		"packaging",
		"requests",
		"slumber",
		"sphinx",
		"sphinxcontrib-domaintools",
		]

bad_example_requirements = """\
domdf_python_tools>=0.4.8
packaging>=20.4
?==requests>=2.24.0
slumber$$$$0.7.1
sphinx>=3.0.3
sphinxcontrib-domaintools==0.3
"""

bad_expected_requirements = [
		"domdf-python-tools",
		"packaging",
		"sphinx",
		"sphinxcontrib-domaintools",
		]


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_requirements_a),
				(bad_example_requirements, bad_expected_requirements),
				]
		)
def test_parse_requirements_txt(tmp_pathplus, contents, expects):
	(tmp_pathplus / "requirements.txt").write_text(contents)

	assert parse_requirements_txt(tmp_pathplus) == expects


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_requirements_a),
				(bad_example_requirements, bad_expected_requirements),
				]
		)
def test_seed_intersphinx_mapping_pyproject(tmp_pathplus, contents, expects):
	data = {"project": {"dependencies": contents.splitlines()}}
	(tmp_pathplus / "pyproject.toml").write_clean(toml.dumps(data))

	assert parse_pyproject_toml(tmp_pathplus) == expects


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_requirements_a),
				(bad_example_requirements, bad_expected_requirements),
				]
		)
def test_seed_intersphinx_mapping_flit(tmp_pathplus, contents, expects):
	data = {"tool": {"flit": {"metadata": {"requires": contents.splitlines()}}}}
	(tmp_pathplus / "pyproject.toml").write_clean(toml.dumps(data))

	assert parse_flit_requirements(tmp_pathplus) == expects
