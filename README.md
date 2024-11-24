# Auto_diff package 

A Python package that performs automatic differentiation using dual numbers.

## Features

* Main file of the project "dual.py" with core functions and attributes:
    * Basic arithmetic operations for dual numbers
    * Other essential functions for automatic differentiation (sin,cos,exp,..)

* A comprehensive test suite that civer a meaningful range of cases. You can execute these tests with pytest by running the command:

```bash
pytest -s tests/*
```

## Installation

Ensure you have Python 3.9 or higher. 
You can install the package and its dependencies from source with:

```
pip install -e .
```

## Usage
Below is a quick example of how to use the package:

```python
import dual_autodiff as df

#Creating two instances of dual numbers
x=df.Dual(2,1)
y=df.Dual(2,4)

#Print dual number x
print(x)

#Computing sine using automatic differentiation
x.sin()

#Multiplying two dual numbers
print(x*y)
```

## Documentation

Visit the [documentation page](https://your-readthedocs-url-here).

