# pylint: disable=cyclic-import

# 3rd party
from sphinx.events import EventListener
from sphinx_toolbox.testing import run_setup

# this package
import seed_intersphinx_mapping
from seed_intersphinx_mapping.extension import sphinx_seed_intersphinx_mapping


class MockApp:

	def __init__(self):
		self.config_values = []
		self.directives = []
		self.connections = []

	def add_config_value(self, *args, **kwargs):
		self.config_values.append(args)

	def add_directive(self, *args, **kwargs):
		self.directives.append(args)

	def connect(self, *args, **kwargs):
		self.connections.append(args)


def test_setup():
	result = run_setup(seed_intersphinx_mapping.setup)

	assert result.setup_ret == {
			"version": seed_intersphinx_mapping.__version__,
			"parallel_read_safe": True,
			"parallel_write_safe": True,
			}

	assert result.app.config["pkg_requirements_source"] == "requirements"
	assert result.app.config["repository_root"] == ".."
	assert result.app.events.listeners == {
			"config-inited": [EventListener(0, sphinx_seed_intersphinx_mapping, priority=850)],
			}
