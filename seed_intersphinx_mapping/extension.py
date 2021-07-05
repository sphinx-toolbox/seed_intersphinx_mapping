#!/usr/bin/env python3
#
#  extension.py
"""
Sphinx-specific functionality.
"""
#
#  Copyright © 2020-2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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
from seed_intersphinx_mapping.requirements_parsers import (
		parse_flit_requirements,
		parse_pyproject_toml,
		parse_requirements_txt
		)

__all__ = ["sphinx_seed_intersphinx_mapping", "setup"]


def sphinx_seed_intersphinx_mapping(app: Sphinx, config: Config) -> None:
	"""
	Updates the ``intersphinx_mapping`` dictionary in the sphinx configuration.
	to include the documentation for the project's requirements.

	:confval:`pkg_requirements_source` may be one of:

	* A list of directories (relative to :confval:`repository_root`)
	  in which to search for ``requirements.txt`` files.
	  Any files found will be used to compile the list of requirements.

	* The string ``'requirements'``.
	  The list of requirements will be determined from the ``requirements.txt`` file
	  in the directory given by the :confval:`repository_root` option.

	* The string ``'pyproject'`` (or ``'pyproject.toml'``).
	  The list  will be parsed from the ``[project.dependencies]`` table of the
	  ``pyproject.toml`` file in the :confval:`repository_root`.

	  .. seealso:: :pep:`621` -- Storing project metadata in pyproject.toml

	* The string ``'flit'``.
	  The list  will be parsed from the ``[tool.flit.metadata.requires]`` table of the
	  ``pyproject.toml`` file in the :confval:`repository_root`.

	:param app:
	:param config:
	"""

	# this package
	from seed_intersphinx_mapping import seed_intersphinx_mapping

	repo_root = os.path.abspath(pathlib.Path(app.srcdir) / config.repository_root)
	config.repository_root = repo_root  # type: ignore

	if isinstance(config.pkg_requirements_source, list):
		requirements = []

		for directory in config.pkg_requirements_source:
			requirements.extend(parse_requirements_txt(os.path.join(repo_root, directory)))

		requirements = sorted(set(requirements))

	elif config.pkg_requirements_source == "requirements":
		requirements = parse_requirements_txt(repo_root)

	elif config.pkg_requirements_source == "flit":
		requirements = parse_flit_requirements(repo_root)

	elif config.pkg_requirements_source.startswith("pyproject"):
		requirements = parse_pyproject_toml(repo_root)

	else:  # pragma: no cover
		raise NotImplementedError(f"Unsupported requirements source '{config.pkg_requirements_source}'")

	for name, (uri, inv) in seed_intersphinx_mapping(*requirements).items():
		if name not in config.intersphinx_mapping:
			config.intersphinx_mapping[name] = (name, (uri, (inv, )))

	# from pprint import pprint
	# pprint(config.intersphinx_mapping)
	# input(">")


def setup(app: Sphinx) -> Dict[str, Any]:
	"""
	Setup :mod:`seed_intersphinx_mapping`.

	:param app:
	"""

	# this package
	from seed_intersphinx_mapping import __version__

	app.setup_extension("sphinx.ext.intersphinx")

	# Either:
	# - "requirements"
	# - a list of directories containing requirements.txt files relative to the repository root
	# - "pyproject" / "pyproject.toml"
	# - "flit"
	app.add_config_value("pkg_requirements_source", "requirements", "html")

	# Location of repository directory relative to documentation source directory
	app.add_config_value("repository_root", "..", "html", types=[str, pathlib.Path, os.PathLike])

	app.connect("config-inited", sphinx_seed_intersphinx_mapping, priority=850)

	return {
			"version": __version__,
			"parallel_read_safe": True,
			"parallel_write_safe": True,
			}
