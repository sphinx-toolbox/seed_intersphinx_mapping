"""
Checks the top 4000 packages on PyPI to see whether they have a documentation URL that
``seed_intersphinx_mapping`` can understand.
"""

# 3rd party
# Download hugovk's list of top 4000 most downloaded packages
import requests

# this package
from seed_intersphinx_mapping import get_sphinx_doc_url

url = "https://hugovk.github.io/top-pypi-packages/top-pypi-packages.json"
top_packages = [p["project"] for p in requests.get(url).json()["rows"]]

print(top_packages)

YES = '✔'
NO = '✘'

for project in top_packages:
	print(project, end='')

	try:
		doc_url = get_sphinx_doc_url(project)
		print(f" {YES} : {doc_url}")
	except ValueError as e:
		print(f" {NO} : {e}")

	input(">>>")
