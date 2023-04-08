# Compile with:
# python setup.py build_ext --inplace --force
from setuptools import setup
from Cython.Build import cythonize

setup(
    name="vscode-python-bug",
    ext_modules=cythonize("testissue.pyx", language_level=3),
    zip_safe=False
)
