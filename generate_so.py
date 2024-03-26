#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:12:57 2024

@author: danyvarghese
"""

from Cython.Build import cythonize
from setuptools import setup, Extension
setup(  name='PyGol',
        version='1.0',
        py_modules=['PyGol'],
        ext_modules =
            cythonize(Extension("PyGol",
                        # the extension name
                sources=["PyGol.c"],
                        # the Cython source and additional C++ source files
                language="c++", # generate and compile C++ code
                                )
                        )
    )


#python3 generate_so.py build_ext --inplace