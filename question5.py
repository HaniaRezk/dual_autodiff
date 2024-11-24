import matplotlib.pyplot as plt
import dual_autodiff as df
import numpy as np
import time
import functools

def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Executing: ",func.__name__)
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("Execution time for this function is: ", end-start)
        return result
    return wrapper


#Derivative using dual numbers
@time_decorator
def f_dual(x):
    return (x.cos()*x.square() + (x.sin()).log())

@time_decorator
def f_analytical(x):
    return (2*x*np.cos(x)+x**2*-np.sin(x)+(np.cos(x)/np.sin(x)))

def f(x):
    return np.log(np.sin(x))+x**2*np.cos(x)

def f_numerically(x,h):
    return (f(x+h)-f(x))/h

x=df.Dual(1.5,1.0)
result_dual=f_dual(x).dual
result_analytical=f_analytical(1.5)
print("Derivative of f(x) using dual numbers is ", result_dual)
print("Analytical derivative of f(x)  is ", result_analytical)
print("Numerical derivative of f(x), with step size= 1e-10 is ", f_numerically(1.5,1e-10))

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


