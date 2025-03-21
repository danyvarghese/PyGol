
from setuptools import setup, Extension, find_packages

module = Extension('PyGol', sources=['PyGol.c'])

setup(
    name='PyGol',
    version='1.0',
    description='PyGol is an ILP system',
    author='Dany Varghese',
    author_email='dany.varghese@surrey.ac.uk',
    url='https://github.com/danyvarghese/PyGol',  
    packages=find_packages(),
    ext_modules=[module],
    install_requires=[
        'graphviz',
        'tqdm',
        'numpy',
        'more-itertools',
        'texttable',
        'Pillow',
        'IPython',
        'requests',
        'beautifulsoup4',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
