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
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/seed_intersphinx_mapping/latest?logo=read-the-docs
	:target: https://seed_intersphinx_mapping.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/workflows/Docs%20Check/badge.svg
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/workflows/Linux/badge.svg
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/workflows/Windows/badge.svg
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/workflows/macOS/badge.svg
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/workflows/Flake8/badge.svg
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/workflows/mypy/badge.svg
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/sphinx-toolbox/seed_intersphinx_mapping/requirements.svg?branch=master
	:target: https://requires.io/github/sphinx-toolbox/seed_intersphinx_mapping/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/sphinx-toolbox/seed_intersphinx_mapping/master?logo=coveralls
	:target: https://coveralls.io/github/sphinx-toolbox/seed_intersphinx_mapping?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sphinx-toolbox/seed_intersphinx_mapping?logo=codefactor
	:target: https://www.codefactor.io/repository/github/sphinx-toolbox/seed_intersphinx_mapping
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

.. |license| image:: https://img.shields.io/github/license/sphinx-toolbox/seed_intersphinx_mapping
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/sphinx-toolbox/seed_intersphinx_mapping
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/seed_intersphinx_mapping/v0.3.0
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/seed_intersphinx_mapping
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/seed_intersphinx_mapping
	:target: https://pypi.org/project/seed_intersphinx_mapping/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/sphinx-toolbox/seed_intersphinx_mapping/master.svg
	:target: https://results.pre-commit.ci/latest/github/sphinx-toolbox/seed_intersphinx_mapping/master
	:alt: pre-commit.ci status

.. end shields

|

Installation
--------------

.. start installation

``seed_intersphinx_mapping`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install seed_intersphinx_mapping

.. end installation


Enable ``seed_intersphinx_mapping`` by adding "seed_intersphinx_mapping" to the ``extensions`` variable in ``conf.py``:

.. code-block:: python

    extensions = [
		...
		"seed_intersphinx_mapping",
		]

For more information see https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions .
