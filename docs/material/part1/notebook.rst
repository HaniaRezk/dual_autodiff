Dual_autodiff Package structure
==========================================

This section provides an overview of our package structure, to clarify the names and hierarchy of our files.

.. code-block:: bash

    .
    ├── pyproject.toml               # Configuration 
    ├── requirements.txt                  
    ├── dual_autodiff/               # Package folder with codes
    │   ├── __init__.py
    │   ├── dual.py                  # Dual class
    ├── dist/                        # Distribution files
    ├── docs/                        # Documentation files
    │   ├── Makefile                 # Commands to build the documentation
    │   ├── conf.py                  # Configuration of the documentation
    │   ├── index.rst                # The main page of the documentation
    │   ├── dual_autodiff.ipynb       # Tutorial notebook
    │   ├──Question5.ipynb            # Code for question 5 of the coursework
    │   ├── material/                # Notebooks for different parts of the documentation
    └── tests/                       # Test folder
    │   ├── autodiff_tools.py        # Test suite for Dual class


