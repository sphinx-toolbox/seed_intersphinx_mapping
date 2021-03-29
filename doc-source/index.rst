#########################
seed_intersphinx_mapping
#########################

.. start short_desc

.. documentation-summary::

.. end short_desc

.. start shields

.. only:: html

	.. list-table::
		:stub-columns: 1
		:widths: 10 90

		* - Docs
		  - |docs| |docs_check|
		* - Tests
		  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
		* - PyPI
		  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
		* - Anaconda
		  - |conda-version| |conda-platform|
		* - Activity
		  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
		* - QA
		  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
		* - Other
		  - |license| |language| |requires|

	.. |docs| rtfd-shield::
		:project: seed_intersphinx_mapping
		:alt: Documentation Build Status

	.. |docs_check| actions-shield::
		:workflow: Docs Check
		:alt: Docs Check Status

	.. |actions_linux| actions-shield::
		:workflow: Linux
		:alt: Linux Test Status

	.. |actions_windows| actions-shield::
		:workflow: Windows
		:alt: Windows Test Status

	.. |actions_macos| actions-shield::
		:workflow: macOS
		:alt: macOS Test Status

	.. |actions_flake8| actions-shield::
		:workflow: Flake8
		:alt: Flake8 Status

	.. |actions_mypy| actions-shield::
		:workflow: mypy
		:alt: mypy status

	.. |requires| requires-io-shield::
		:alt: Requirements Status

	.. |coveralls| coveralls-shield::
		:alt: Coverage

	.. |codefactor| codefactor-shield::
		:alt: CodeFactor Grade

	.. |pypi-version| pypi-shield::
		:project: seed_intersphinx_mapping
		:version:
		:alt: PyPI - Package Version

	.. |supported-versions| pypi-shield::
		:project: seed_intersphinx_mapping
		:py-versions:
		:alt: PyPI - Supported Python Versions

	.. |supported-implementations| pypi-shield::
		:project: seed_intersphinx_mapping
		:implementations:
		:alt: PyPI - Supported Implementations

	.. |wheel| pypi-shield::
		:project: seed_intersphinx_mapping
		:wheel:
		:alt: PyPI - Wheel

	.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/seed_intersphinx_mapping?logo=anaconda
		:target: https://anaconda.org/domdfcoding/seed_intersphinx_mapping
		:alt: Conda - Package Version

	.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/seed_intersphinx_mapping?label=conda%7Cplatform
		:target: https://anaconda.org/domdfcoding/seed_intersphinx_mapping
		:alt: Conda - Platform

	.. |license| github-shield::
		:license:
		:alt: License

	.. |language| github-shield::
		:top-language:
		:alt: GitHub top language

	.. |commits-since| github-shield::
		:commits-since: v0.4.0
		:alt: GitHub commits since tagged version

	.. |commits-latest| github-shield::
		:last-commit:
		:alt: GitHub last commit

	.. |maintained| maintained-shield:: 2021
		:alt: Maintenance

	.. |pypi-downloads| pypi-shield::
		:project: seed_intersphinx_mapping
		:downloads: month
		:alt: PyPI - Downloads

	.. |pre_commit_ci| pre-commit-ci-shield::
		:alt: pre-commit.ci status

.. end shields

Installation
---------------

.. start installation

.. installation:: seed_intersphinx_mapping
	:pypi:
	:github:
	:anaconda:
	:conda-channels: conda-forge, domdfcoding

.. end installation


.. extensions:: seed_intersphinx_mapping

Configuration
-----------------

.. confval:: pkg_requirements_source

	The requirements source. This may be one of:

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


.. confval:: repository_root

	The path to the repository root, relative to the Sphinx source directory.

	E.g., for this repository structure:

	::

		.
		├── LICENSE
		├── README.rst
		├── doc-source  # <- this is the Sphinx source directory
		│   ├── index.rst
		│   └── conf.py
		├── requirements.txt  # <- this is the file containing the requirements
		├── seed_intersphinx_mapping
		│   └── __init__.py
		├── setup.py
		├── tests
		└── tox.ini

	the value would be ``..``, which is the default.


Caching
--------

``seed_intersphinx_mapping`` caches the documentation URLs for PyPI packages.
The cache can be cleared as follows:

.. prompt:: bash

	python3 -m seed_intersphinx_mapping

.. TODO:: automatic cache clearing


Contents
--------

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
	:caption: Contributing

	contributing
	Source

.. start links

.. only:: html

	View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

	`Browse the GitHub Repository <https://github.com/sphinx-toolbox/seed_intersphinx_mapping>`__

.. end links
