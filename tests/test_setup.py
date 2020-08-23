# this package
import seed_intersphinx_mapping
from seed_intersphinx_mapping.extension import sphinx_purge_cache, sphinx_seed_intersphinx_mapping


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
	app = MockApp()

	assert seed_intersphinx_mapping.setup(app=app) == {  # type: ignore
		"version": seed_intersphinx_mapping.__version__,
		"parallel_read_safe": True,
		"parallel_write_safe": True,
		}

	assert app.config_values == [
			("pkg_requirements_source", "requirements", "html"),
			("repository_root", "..", "html"),
			]
	assert app.connections == [
			("config-inited", sphinx_seed_intersphinx_mapping),
			("env-purge-doc", sphinx_purge_cache),
			]
