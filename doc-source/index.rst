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
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor| |pre_commit_ci|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| rtfd-shield::
	:project: seed_intersphinx_mapping
	:alt: Documentation Build Status

.. |docs_check| actions-shield::
	:workflow: Docs Check
	:alt: Docs Check Status

.. |travis| actions-shield::
	:workflow: Linux Tests
	:alt: Linux Test Status

.. |actions_windows| actions-shield::
	:workflow: Windows Tests
	:alt: Windows Test Status

.. |actions_macos| actions-shield::
	:workflow: macOS Tests
	:alt: macOS Test Status

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

.. |license| github-shield::
	:license:
	:alt: License

.. |language| github-shield::
	:top-language:
	:alt: GitHub top language

.. |commits-since| github-shield::
	:commits-since: v0.3.0
	:alt: GitHub commits since tagged version

.. |commits-latest| github-shield::
	:last-commit:
	:alt: GitHub last commit

.. |maintained| maintained-shield:: 2020
	:alt: Maintenance

.. |pre_commit| pre-commit-shield::
	:alt: pre-commit

.. |pre_commit_ci| pre-commit-ci-shield::
	:alt: pre-commit.ci status

.. end shields

Installation
---------------

.. start installation

.. installation:: seed_intersphinx_mapping
	:pypi:
	:github:

.. end installation


.. extensions:: seed_intersphinx_mapping

Configuration
-----------------

.. confval:: pkg_requirements_source

	The requirements source.

	* If this is a list, it is taken to be a list of directories
	  in which to search for ``requirements.txt`` files.
	  Any files found will be used to compile the list of requirements.

	* If this is the string ``requirements``,
	  the list of requirements will be determined from the ``requirements.txt`` file
	  in the  directory given by the :confval:`pkg_requirements_source` option.

	Currently, no other sources are supported.


.. confval:: repository_root

	The path to the repository root, relative to the Sphinx source directory.

	E.g., for this repository structure:

	::

		.
		├── LICENSE
		├── README.rst
		├── doc-source  # <- this is the Sphinx source directory
		|   ├── index.rst
		|   └── conf.py
		├── requirements.txt  # <- this is the file containing the requirements
		├── seed_intersphinx_mapping
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

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/seed_intersphinx_mapping>`__

.. end links
