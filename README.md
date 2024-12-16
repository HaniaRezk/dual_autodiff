## Dual_autodiff Package 

A Python package that performs automatic differentiation using dual numbers.

## Dual_autodiff_x Package 

The Cythonized version of the dual_autodiff package.
* The "Wheels_contents" folder contains the two wheels of this cynthonised package.

## Features of Dual_autodiff Package

* Main file of the project "dual.py" with core functions and attributes:
    * Basic arithmetic operations for dual numbers
    * Other essential functions for automatic differentiation (sin,cos,exp,..)
    
* "Tests" folder that contains:
    * "autodiff_tools": a comprehensive test suite that covers a meaningful range of cases. 

* "Docs" folder that generates the documentation of the package, it contains:
    * "question5.ipynb": a notebook that computes the derivative of a function f(x) using dual numbers, and compares it to the analytical and numerical derivatives.
    * "dual_autodiff.ipynb": a tutorial notebook that contains examples of using the package. It also compares the performances of the pure python package and the cynthonised version.


## Installation
Ensure you have the latest version of pip 24.3.1 installed in your environment.
You can upgrade pip by running the command:
```
pip install --upgrade pip
```

Ensure you have Python 3.9 or higher. 

You can install the dual_autodiff package and its dependencies from the package source with:

```
pip install -e .
```

You can install the dual_autodiff_x from the "Wheels_contents" folder with:

```
pip install dual_autodiff_x_ <name_of_wheel >.whl
```

## Tests
After having installed the dual_autodiff package, you can execute the tests with pytest by running the command, from the dual_autodiff package folder:

```bash
pytest -s tests/*
```

If `pytest` is not installed in your environment, you can install it with:
```bash
pip install pytest

```
## Documentation

A Sphinx documentation was used to generate the documentation for the dual_autodiff package. After having installed the package, you can generate the html documentation page by running the following command from the docs folder of the dual_autodiff package folder.

```bash
make install
make clean
make html
```

The documentation can be viewed by opening docs/build/html/index.html in a web browser.
The make install command installs all the necessary modules for the documentation.

## Tutorial notebook
The notebook "dual_autodiff.ipynb" contains examples of how to use the dual_autodiff and dual_autodiff_x packages. It also compares the performances of the pure python package and the cynthonised version.

Make sure to run 'make install' from the docs folder (of the dual_autodiff package folder) in your kernel environment to install the necessary libraries for running this notebook. Make sure to also install the cynthonized package and the pure python package in your kernel environment.

## question5 notebook
The notebook "question5.ipynb" contains that computes the derivative of a function f(x) using dual numbers, and compares it to the analytical and numerical derivatives.
