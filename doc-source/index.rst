#########################
seed_intersphinx_mapping
#########################

.. start short_desc

.. documentation-summary::
	:meta:

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
		  - |codefactor| |actions_flake8| |actions_mypy|
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
		:commits-since: v0.5.0
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

.. end shields

This avoids having to manually compile (and keep updated) a mapping like:

.. code-block:: python

	intersphinx_mapping = {
		"attrs": ('https://www.attrs.org/en/stable/', None),
		"Flask": ('https://flask.palletsprojects.com/en/1.1.x/', None),
		"matplotlib": ('https://matplotlib.org/stable/', None),
		"numpy": ('https://numpy.org/doc/stable/', None),
		"pandas": ('https://pandas.pydata.org/docs/', None),
		"Pyramid": ('https://docs.pylonsproject.org/projects/pyramid/en/latest/', None),
		"scikit-learn": ('https://scikit-learn.org/stable/', None),
		"scipy": ('https://docs.scipy.org/doc/scipy/reference/', None),
		"Sphinx": ('https://www.sphinx-doc.org/en/stable/', None),
	}
	# Source: https://gist.github.com/bskinn/0e164963428d4b51017cebdb6cda5209

.. note::

	Not all projects include a link to their documentation in the Project-URL_ field of Python's `core metadata`_.
	Why not submit a `pull request`_ to them to include it?

	For `setuptools' <https://setuptools.readthedocs.io/en/latest/>`_ ``setup.cfg``, this would look like:

	.. code-block:: ini

		project_urls =
			Documentation = <documentation_url, e.g. https://domdf-python-tools.readthedocs.io/en/latest>

	Or, in :pep:`pyproject.toml <621>`:

	.. code-block:: toml

		[project.urls]
		Documentation = "<documentation_url, e.g. https://domdf-python-tools.readthedocs.io/en/latest>"

	In the meantime you will still need to manually include an entry for that project in your ``intersphinx_mapping``.

.. seealso:: The Sphinx documentation for :mod:`sphinx.ext.intersphinx`.

.. _Project-URL: https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
.. _core metadata: https://packaging.python.org/specifications/core-metadata
.. _pull request: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests

Contents
--------

.. html-section::

.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3

	usage
	api/index
	Source

.. sidebar-links::
	:caption: Links
	:github:
	:pypi: seed_intersphinx_mapping

	Contributing Guide <https://contributing-to-sphinx-toolbox.readthedocs.io/en/latest/>

.. start links

.. only:: html

	View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

	:github:repo:`Browse the GitHub Repository <sphinx-toolbox/seed_intersphinx_mapping>`

.. end links
