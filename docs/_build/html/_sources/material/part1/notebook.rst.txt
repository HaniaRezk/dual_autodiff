Package structure
==========================================

This section provides an overview of our package structure, to clarify the names and hierarchy of our files.

.. code-block:: bash

    .
    ├── pyproject.toml               # Configuration 
    ├── README.md                    # Instructions
    ├── dual_autodiff/               # Package folder with codes
    │   ├── __init__.py
    │   ├── version.py               #Manage package versions
    │   ├── dual.py                  # Dual class
    ├── dist/                        # Distribution files
    ├── docs/                        # Documentation files
    │   ├── Makefile                 # Commands to build the documentation
    │   ├── requirements.txt              
    │   ├── conf.py                  # Configuration of the documentation
    │   ├── index.rst                # The main page of the documentation
    │   ├── material/                # Notbeooks for different parts of the documentation
    └── tests/                       # Test folder
    │   ├── autodiff_tools.py        # Test suite for Dual class
    └── Question5.py                 # Code for question 5 of the coursework

