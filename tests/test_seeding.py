# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

# this package
from seed_intersphinx_mapping import seed_intersphinx_mapping
from tests.test_requirements_parsers import bad_example_requirements, example_requirements_a

expected_mapping_a = {
		"domdf-python-tools": ("https://domdf-python-tools.readthedocs.io/en/latest/", None),
		"packaging": ("https://packaging.pypa.io/en/latest/", None),
		"requests": ("https://requests.readthedocs.io/en/master/", None),
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

	assert seed_intersphinx_mapping(tmp_pathplus) == expects
	err = capsys.readouterr().err
	assert err == "WARNING: Unable to determine documentation url for project sphinxcontrib-domaintools\n"
