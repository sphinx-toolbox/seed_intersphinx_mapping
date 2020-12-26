#!/usr/bin/env python3
#
#  extension.py
"""
Sphinx-specific functionality.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import os
import pathlib
from typing import Any, Dict

# 3rd party
from sphinx.application import Sphinx
from sphinx.config import Config

# this package
from seed_intersphinx_mapping.core import seed_intersphinx_mapping

__all__ = ["sphinx_seed_intersphinx_mapping", "setup"]


def sphinx_seed_intersphinx_mapping(app: Sphinx, config: Config) -> None:
	"""
	Updates the ``intersphinx_mapping`` dictionary in the sphinx configuration.
	to include the documentation for the project's requirements.

	If :confval:`pkg_requirements_source` is a list, it is taken to be a list of directories
	in which to search for ``requirements.txt`` files. Any files found will be used to compile
	the list of requirements.

	Otherwise, if :confval:`pkg_requirements_source` is the string ``requirements``,
	the list of requirements will be determined from the ``requirements.txt`` file
	in the  directory given by the :confval:`repository_root` option.

	:param app:
	:param config:
	"""

	repo_root = os.path.abspath(pathlib.Path(app.srcdir) / config.repository_root)
	config.repository_root = repo_root  # type: ignore

	if config.pkg_requirements_source == "requirements":
		for name, (uri, inv) in seed_intersphinx_mapping(repo_root).items():
			config.intersphinx_mapping[name] = (name, (uri, (inv, )))

	elif isinstance(config.pkg_requirements_source, list):
		for directory in config.pkg_requirements_source:
			for name, (uri, inv) in seed_intersphinx_mapping(repo_root / directory).items():
				config.intersphinx_mapping[name] = (name, (uri, (inv, )))

	else:  # pragma: no cover
		raise NotImplementedError(f"Unsupported requirements source '{config.pkg_requirements_source}'")

	# from pprint import pprint
	# pprint(config.intersphinx_mapping)
	# input(">")


def setup(app: Sphinx) -> Dict[str, Any]:
	"""
	Setup Sphinx Extension.

	:param app:

	:return:
	"""

	# this package
	from seed_intersphinx_mapping import __version__

	# Currently, only "requirements" or a list of directories containing requirements.txt files relative to the repository root,
	app.add_config_value("pkg_requirements_source", "requirements", "html")

	# Location of repository directory relative to documentation source directory
	app.add_config_value("repository_root", "..", "html", types=[str, pathlib.Path, os.PathLike])

	app.connect("config-inited", sphinx_seed_intersphinx_mapping, priority=850)

	return {
			"version": __version__,
			"parallel_read_safe": True,
			"parallel_write_safe": True,
			}
