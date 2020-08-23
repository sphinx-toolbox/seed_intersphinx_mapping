#!/usr/bin/env python3
#
#  requirements_parsers.py
"""
Contains functions for parsing requirements.

.. TODO:: Other formats, e.g. setup.cfg, flit, poetry
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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
from typing import List

# 3rd party
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.typing import PathLike
from packaging.requirements import InvalidRequirement, Requirement

__all__ = ["parse_requirements_txt"]


def parse_requirements_txt(base_dir: PathLike) -> List[str]:
	"""
	Returns a list of package names listed in the ``requirements.txt`` file..

	:param base_dir: The directory in which to find the ``requirements.txt`` file.
	"""

	requirements = []

	for line in (PathPlus(base_dir) / "requirements.txt").read_text().split("\n"):
		if not line.startswith("#"):
			try:
				requirements.append(Requirement(line).name)
			except InvalidRequirement:
				pass

	return requirements
