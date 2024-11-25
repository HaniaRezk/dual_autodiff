Test suite
==========================================

This section provides an overview of the `test suite` implemented for the Dual class.

For each function in the Dual class, a test was implemented to make sure it performs as expected.

Details
----------------------------------------
For functions that redefine operators (eg. , `+`, `-`, `*`, `/` , `==`, `!=`) two tests were performed:


1- A first test for the operations between two dual numbers 

2- A second test for these operations between a dual number and a scalar 

For the functions that can raise warnings, tests were also performed using illegal inputs to make sure the function returns a NAN.

Tests
----------------------------------------
.. automodule:: tests.autodiff_tools
    :members:
    :undoc-members:
    :show-inheritance:
    


