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

Ensure you have Python 3.9 or higher installed in your environment.
You can check your current Python version by running:
```bash
python --version
```
If Python 3.9 or higher is not installed, you can download it from the official Python website.

Ensure you have the latest version of pip 24.3.1 installed in your environment.
You can upgrade pip by running the command:
```
pip install --upgrade pip

```

## Installation of dual_autodiff package

You can install the dual_autodiff package and its dependencies from the package source by running:
```
pip install -r requirements.txt
pip install -e .
```

The ```pip install -r requirements.txt``` command installs all the necessary modules for the documentation and test suite.

## Tests

After having installed the dual_autodiff package and the requirements.txt file, you can execute the tests with pytest by running the following command, from the dual_autodiff package folder:

```bash
pytest -s tests/*
```

## Documentation
After having installed the package and the requirements.txt file, you can generate the html documentation page by running the following command from the docs folder of the dual_autodiff package folder.

```bash
make clean
make html
```
The documentation can be viewed by opening dual_autodiff/docs/build/html/index.html in a web browser.

OR 

You can view the documentation directly by unzipping the folder ready_build.zip (documentation built in advance) in dual_autodiff. In this case the documentation can be viewed by opening dual_autodiff/ready_build/html/index.html in a web browser.

# Running the Notebooks in the docs folder

Make sure to install dual_autodiff, dual_autodiff_x and requirements.txt in your kernel environment, before running the following notebooks from the docs folder of dual_autodiff: dual_autodiff.ipynb and question5.ipynb.


## Virtual environments and kernels of the notebooks

If you are using a virtual environment to install the previous packages, here's how you can configure a kernel to run the notebooks within this environment.

### Creating the Kernel

Use the following commands to register your virtual environment as a kernel:

```bash
pip install ipykernel
python3.9 -m ipykernel install --user --name=name_of_your_env --display-name "Chosen Display Name"
```

### Selecting the kernel in your notebook

1. Open your notebook.  
2. Navigate to the **Kernel** menu and choose **Change kernel**.  
3. Select the kernel with your chosen display name.