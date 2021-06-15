#!/bin/bash
# This file is managed by 'repo_helper'. Don't edit it directly.

set -e -x

python -m mkrecipe --type wheel || exit 1

$CONDA/bin/conda config --set always_yes yes --set changeps1 no
$CONDA/bin/conda install conda-build
$CONDA/bin/conda install anaconda-client
$CONDA/bin/conda info -a

$CONDA/bin/conda config --add channels conda-forge || exit 1
$CONDA/bin/conda config --add channels domdfcoding || exit 1

$CONDA/bin/conda build conda -c conda-forge -c domdfcoding --output-folder conda/dist --skip-existing

exit 0
