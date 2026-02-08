credentials are in ~/.pypirc

- rm -rf build/ dist/ *.egg-info/
- update version in setup.py and ./eaglebirth/__init__.py
- python3 -m pip install --upgrade build
- python3 -m build
- python3 -m pip install --upgrade twine


Test first (Recommended)
It is highly recommended to upload to TestPyPI first to make sure your metadata looks correct.
- python3 -m twine upload --repository testpypi dist/*

Upload to live PyPI
- python3 -m twine upload --repository pypi dist/*