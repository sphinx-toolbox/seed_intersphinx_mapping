# 3rd party
import pytest
from domdf_python_tools.paths import PathPlus

# this package
from seed_intersphinx_mapping import seed_intersphinx_mapping
from tests.test_requirements_parsers import bad_example_requirements, example_requirements_a

expected_mapping_a = {
		"domdf_python_tools": ("https://domdf-python-tools.readthedocs.io/en/latest/", None),
		"packaging": ("https://packaging.pypa.io/en/latest/", None),
		"requests": ("https://requests.readthedocs.io/en/master/", None),
		"slumber": ("https://slumber.readthedocs.io/en/v0.6.0/", None),
		}
bad_expected_mapping = {
		"domdf_python_tools": ("https://domdf-python-tools.readthedocs.io/en/latest/", None),
		"packaging": ("https://packaging.pypa.io/en/latest/", None),
		}


@pytest.mark.parametrize(
		"contents, expects", [
				(example_requirements_a, expected_mapping_a),
				(bad_example_requirements, bad_expected_mapping),
				]
		)
def test_seed_intersphinx_mapping(tmpdir, contents, expects):
	(PathPlus(tmpdir) / "requirements.txt").write_text(contents)

	with pytest.warns(UserWarning) as w:
		assert seed_intersphinx_mapping(tmpdir) == expects
	assert len(w) == 1
