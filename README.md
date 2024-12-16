## Dual_autodiff Package 

A Python package that performs automatic differentiation using dual numbers.

## Dual_autodiff_x Package 

The Cythonized version of the dual_autodiff package.

## Wheelhouse folder
* The "Wheelhouse" folder contains the two wheels of the cynthonised package "dual_autodiff_x".
    * dual_autodiff_x-0.0.5-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl
    * dual_autodiff_x-0.0.5-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl

## Features of Dual_autodiff Package

* Main file of the project "dual.py" with core functions and attributes:
    * Basic arithmetic operations for dual numbers
    * Other essential functions for automatic differentiation (sin,cos,exp,..)
    
* "Tests" folder that contains:
    * "autodiff_tools": a comprehensive test suite that covers a meaningful range of cases. 

* "Docs" folder that generates the documentation of the package, it contains:
    * "question5.ipynb": a notebook that computes the derivative of a function f(x) using dual numbers, and compares it to the analytical and numerical derivatives.
    * "dual_autodiff.ipynb": a tutorial notebook that contains examples of using the package. It also compares the performances of the pure python package and the cynthonised version.


## Installation: General notes
Ensure you have the latest version of pip 24.3.1 installed in your environment.
You can upgrade pip by running the command:
```
pip install --upgrade pip

```
Ensure you have Python 3.9 or higher. 

## Installation of dual_autodiff package

You can install the dual_autodiff package and its dependencies from the package source with:
```
pip install -r requirements.txt
pip install -e .
```

The "pip install -r requirements.txt" command installs all the necessary modules for the documentation and test suite.

## Installation of dual_autodiff_x package

You can install the dual_autodiff_x package from the package source with:

```
pip install -e .
```
OR 

You can install the dual_autodiff_x package from its wheels from the "wheelhouse" folder from the precompiled binary distributions of the package built for Python3.10 and Python3.11 by running:

```
pip install dual_autodiff_x_ <name_of_wheel >.whl
```

## Tests

After having installed the dual_autodiff package and the requirements.txt file, you can execute the tests with pytest by running the command, from the dual_autodiff package folder:

```bash
pytest -s tests/*
```

## Documentation

A Sphinx documentation was used to generate the documentation for the dual_autodiff package. After having installed the package and the requirements.txt file, you can generate the html documentation page by running the following command from the docs folder of the dual_autodiff package folder.

```bash
make clean
make html
```

The documentation can be viewed by opening docs/build/html/index.html in a web browser.

# Running the Notebooks in the docs folder

Make sure to install dual_autodiff, dual_autodiff_x and requirements.txt in your kernel environment, before running the following notebooks.


## dual_autodiff notebook
The notebook "dual_autodiff.ipynb" contains examples of how to use the dual_autodiff and dual_autodiff_x packages. It also compares the performances of the pure python package and the cynthonised version.

## question5 notebook
The notebook "question5.ipynb" computes the derivatives of a function f(x) using dual numbers, and compares it to the analytical and numerical derivatives.
