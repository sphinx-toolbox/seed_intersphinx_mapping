#!/bin/bash
# This file is managed by 'repo_helper'. Don't edit it directly.

set -e -x

$CONDA/bin/conda config --set always_yes yes --set changeps1 no
$CONDA/bin/conda update -q conda
$CONDA/bin/conda install anaconda-client
$CONDA/bin/conda info -a

for f in conda/dist/noarch/seed_intersphinx_mapping-*.tar.bz2; do
  [ -e "$f" ] || continue
  echo "$f"
  $CONDA/bin/conda install "$f" || exit 1
  echo "Deploying to Anaconda.org..."
  $CONDA/bin/anaconda -t "$ANACONDA_TOKEN" upload "$f" || exit 1
  echo "Successfully deployed to Anaconda.org."
done

exit 0
