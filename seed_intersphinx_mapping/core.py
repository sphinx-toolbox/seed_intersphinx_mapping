#!/usr/bin/env python3
#
#  core.py
"""
Core functionality.
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
import warnings

# 3rd party
from cawdrey.utils import search_dict
from shippinglabel.pypi import PYPI_API

# this package
from seed_intersphinx_mapping import fallback_mapping, get_sphinx_doc_url, seed_intersphinx_mapping

__all__ = ["search_dict", "get_sphinx_doc_url", "fallback_mapping", "seed_intersphinx_mapping", "PYPI_API"]

warnings.warn(
		"seed_intersphinx_mapping.core is deprecated in 0.5.0 and will be removed in 1.0.0. "
		"Import directly from seed_intersphinx_mapping instead.",
		DeprecationWarning,
		)
