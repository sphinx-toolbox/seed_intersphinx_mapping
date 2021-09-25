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
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
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

.. |requires| image:: https://dependency-dash.herokuapp.com/github/sphinx-toolbox/seed_intersphinx_mapping/badge.svg
	:target: https://dependency-dash.herokuapp.com/github/sphinx-toolbox/seed_intersphinx_mapping/
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

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/seed_intersphinx_mapping?logo=anaconda
	:target: https://anaconda.org/domdfcoding/seed_intersphinx_mapping
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/seed_intersphinx_mapping?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/seed_intersphinx_mapping
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/sphinx-toolbox/seed_intersphinx_mapping
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/sphinx-toolbox/seed_intersphinx_mapping
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/seed_intersphinx_mapping/v1.0.0
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/seed_intersphinx_mapping
	:target: https://github.com/sphinx-toolbox/seed_intersphinx_mapping/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/seed_intersphinx_mapping
	:target: https://pypi.org/project/seed_intersphinx_mapping/
	:alt: PyPI - Downloads

.. end shields


This avoids having to manually compile (and keep updated) a mapping like:

.. code-block:: python

	intersphinx_mapping = {
			"attrs": ("https://www.attrs.org/en/stable/", None),
			"Flask": ("https://flask.palletsprojects.com/en/1.1.x/", None),
			"matplotlib": ("https://matplotlib.org/stable/", None),
			"numpy": ("https://numpy.org/doc/stable/", None),
			"pandas": ("https://pandas.pydata.org/docs/", None),
			"Pyramid": ("https://docs.pylonsproject.org/projects/pyramid/en/latest/", None),
			"scikit-learn": ("https://scikit-learn.org/stable/", None),
			"scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
			"Sphinx": ("https://www.sphinx-doc.org/en/stable/", None),
			}
	# Source: https://gist.github.com/bskinn/0e164963428d4b51017cebdb6cda5209


See `the documentation`_ for more information.

**Note:** Not all projects include a link to their documentation in the Project-URL_ field of Python's `core metadata`_.
Why not submit a `pull request`_ to them to include it?

.. _Project-URL: https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
.. _core metadata: https://packaging.python.org/specifications/core-metadata
.. _pull request: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
.. _the documentation: https://seed-intersphinx-mapping.readthedocs.io/en/latest/

Installation
--------------

.. start installation

``seed_intersphinx_mapping`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install seed_intersphinx_mapping

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install seed_intersphinx_mapping

.. end installation


Enable ``seed_intersphinx_mapping`` by adding "seed_intersphinx_mapping" to the ``extensions`` variable in ``conf.py``:

.. code-block:: python

    extensions = [
		...
		"seed_intersphinx_mapping",
		]

For more information see https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions .

See `the documentation`_ for more information on configuring ``seed_intersphinx_mapping``.

.. _the documentation: https://seed-intersphinx-mapping.readthedocs.io/en/latest/
