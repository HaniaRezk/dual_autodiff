import matplotlib.pyplot as plt
import dual_autodiff as df
import numpy as np
import time
import functools

def time_decorator(func):
    """
    A decorator to compute the execution time of each function, and help compare their performances.
    """
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Executing: ",func.__name__)
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("Execution time for this function is: ", end-start)
        return result
    return wrapper


@time_decorator
def f_analytical(x):
    """
    The function that computes analytically the derivative of f(x).

    Parameters:
        x: value at which we want to compute the derivative.

    Returns:
        Analytic derivative
    """
    return (2*x*np.cos(x)+x**2*-np.sin(x)+(np.cos(x)/np.sin(x)))

def f(x):
    """
    The function for which we want to compute the derivatives using different methods.

    Parameters:
        x: value at which we want to compute the value of the function.

    Returns: 
        The function of interest.
    """
    return np.log(np.sin(x))+x**2*np.cos(x)

def f_numerically(x,h):
    """
    The function that computes numerically the derivative of f(x).

    Parameters:
        x: value at which we want to compute the derivative.
        h: step size.

    Returns:
        Numerical derivative.
    """
    return (f(x+h)-f(x))/h

def f_AD(x):
    """
    The function that computes the derivative of f(x) using automatic differentiation.

    Parameters:
        x: value at which we want to compute the derivative.

    Returns:
        Derivative computed using dual numbers.
    """
    x1=df.Dual(x,1.0)
    result=(x1.cos()*x1.square() + (x1.sin()).log())
    return result.dual


result_dual=f_AD(1.5)
result_analytical=f_analytical(1.5)
print("Derivative of f(x) using dual numbers is ", result_dual)
print("Analytical derivative of f(x)  is ", result_analytical)
print("Numerical derivative of f(x), with step size= 1e-10 is ", f_numerically(1.5,1e-10))

def plot_analytical_numerical():
    """
    A function that plots the absolute differences between the analytical and numerical derivatives for different step sizes h.
    """
    numerical_results=[]
    step_size = [1,0.5,0.3,0.01,0.001,0.0001,0.00001,0.000001,1e-7,1e-8,1e-10,1e-11,1e-12,1e14]
    for h in step_size:
        numerical_results.append(f_numerically(1.5,h))

    plt.plot(step_size,np.abs(numerical_results-result_analytical), marker='o', linestyle='--')
    plt.ylabel("Step size")
    plt.yscale('log')
    plt.xlabel("Absolute differences between analytical and numerical derivatives")
    plt.legend()
    plt.grid()
    plt.show()




