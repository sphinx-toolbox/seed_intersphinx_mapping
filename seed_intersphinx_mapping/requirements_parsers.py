#!/usr/bin/env python3
#
#  requirements_parsers.py
"""
Contains functions for parsing requirements.
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
from operator import attrgetter
from typing import List

# 3rd party
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.typing import PathLike
from shippinglabel.requirements import parse_pyproject_dependencies, read_requirements

__all__ = ["parse_flit_requirements", "parse_pyproject_toml", "parse_requirements_txt"]


def parse_requirements_txt(base_dir: PathLike) -> List[str]:
	"""
	Returns a list of package names listed as requirements in the ``requirements.txt`` file.

	:param base_dir: The directory in which to find the ``requirements.txt`` file.
	"""

	requirements, comments, invalid = read_requirements(
		req_file=PathPlus(base_dir) / "requirements.txt",
		include_invalid=True,
		)

	return sorted(map(attrgetter("name"), requirements))


def parse_pyproject_toml(base_dir: PathLike) -> List[str]:
	"""
	Returns a list of package names listed as requirements in the ``pyproject.toml`` file.

	.. versionadded:: 0.4.0

	:param base_dir: The directory in which to find the ``pyproject.toml`` file.
	"""

	requirements = parse_pyproject_dependencies(
			pyproject_file=PathPlus(base_dir) / "pyproject.toml",
			flavour="pep621",
			)

	return sorted(map(attrgetter("name"), requirements))


def parse_flit_requirements(base_dir: PathLike) -> List[str]:
	"""
	Returns a list of package names listed as requirements in the ``[tool.flit]`` section of ``pyproject.toml``.

	.. versionadded:: 0.4.0

	:param base_dir: The directory in which to find the ``pyproject.toml`` file.
	"""

	requirements = parse_pyproject_dependencies(
			pyproject_file=PathPlus(base_dir) / "pyproject.toml",
			flavour="flit",
			)

	return sorted(map(attrgetter("name"), requirements))
