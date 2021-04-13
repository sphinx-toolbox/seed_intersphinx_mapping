=======
Usage
=======

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

.. TODO:: automatic cache clearing, perhaps using ``intersphinx_cache_limit``
