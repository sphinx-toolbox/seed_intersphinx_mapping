#########################
seed_intersphinx_mapping
#########################

.. start short_desc

**Populate the Sphinx 'intersphinx_mapping' dictionary from the project's requirements.**

.. end short_desc

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/seed_intersphinx_mapping/latest?logo=read-the-docs
	:target: https://seed_intersphinx_mapping.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |docs_check| image:: https://github.com/domdfcoding/seed_intersphinx_mapping/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/seed_intersphinx_mapping/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/seed_intersphinx_mapping/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/seed_intersphinx_mapping
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/seed_intersphinx_mapping/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/seed_intersphinx_mapping/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/seed_intersphinx_mapping/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/seed_intersphinx_mapping/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/seed_intersphinx_mapping/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/seed_intersphinx_mapping/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/seed_intersphinx_mapping/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/seed_intersphinx_mapping?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/seed_intersphinx_mapping?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/seed_intersphinx_mapping
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/seed_intersphinx_mapping
	:target: https://pypi.org/project/seed_intersphinx_mapping/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/seed_intersphinx_mapping?logo=python&logoColor=white
	:target: https://pypi.org/project/seed_intersphinx_mapping/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/seed_intersphinx_mapping
	:target: https://pypi.org/project/seed_intersphinx_mapping/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/seed_intersphinx_mapping
	:target: https://pypi.org/project/seed_intersphinx_mapping/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/seed_intersphinx_mapping
	:target: https://github.com/domdfcoding/seed_intersphinx_mapping/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/seed_intersphinx_mapping
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/seed_intersphinx_mapping/v0.1.0
	:target: https://github.com/domdfcoding/seed_intersphinx_mapping/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/seed_intersphinx_mapping
	:target: https://github.com/domdfcoding/seed_intersphinx_mapping/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. end shields

Installation
---------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			python3 -m pip install seed_intersphinx_mapping --user


	.. tab:: from GitHub

		.. prompt:: bash

			python3 -m pip install git+https://github.com/domdfcoding/seed_intersphinx_mapping@master --user

.. end installation


Enable ``seed_intersphinx_mapping`` by adding "seed_intersphinx_mapping" to the ``extensions`` variable in ``conf.py``:

.. code-block:: python

    extensions = [
		...
		"seed_intersphinx_mapping",
		]

For more information see https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions .


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: API Reference
	:glob:

	api/*

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	contributing
	Source

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/seed_intersphinx_mapping>`__

.. end links
