from setuptools import setup, Extension

module = Extension('PyGol', sources=['PyGol.c'])

setup(
    name='PyGol',
    version='1.0',
    description='C extension module for Python',
    ext_modules=[module]
)