# stdlib
from typing import Optional

# 3rd party
from domdf_python_tools.paths import PathPlus
from sphinx.application import Sphinx


def replace_zwsp(app: Sphinx, exception: Optional[Exception] = None):
	if exception:
		return

	if app.builder.name.lower() != "latex":
		return

	output_file = PathPlus(app.builder.outdir) / f"{app.builder.titles[0][1]}.tex"
	output_file.write_clean(output_file.read_text().replace('\u200b', ''))


def setup(app: Sphinx):
	app.connect("build-finished", replace_zwsp)
