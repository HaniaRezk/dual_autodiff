# dual_autodiff/dual.py
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Dual:
    """
    A class that defines a structure for dual numbers and performs standards operations on them.

    Attributes:
        real: real part of the number.
        dual: dual part of the number.
    """
    def __init__(self,real,dual):
        """
        Initializes the dual number using its real and dual part.

        Parameters:
        real: real part of the number.
        dual: dual part of the number.
        """
        self.real=real
        self.dual=dual

    def __str__(self):
        """
        Redefines the readable string form of the class to get the desired output when we use print the dual number.

        Returns:
            String: in the form "Dual(real=number.real, dual=number.dual) "
        """
        string="Dual(real="+ str(self.real) +", dual="+ str(self.dual)+ ")."
        return string

    def __add__(self,x):
        """
        Redefines the ``+`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to add to our current instance.

        Returns:
            dual number: the result of the addition of the current instance and the input (dual number or scalar)
        """
        if isinstance(x, Dual):
            return Dual(x.real+self.real,x.dual+self.dual)
        else:
            return Dual(x + self.real,self.dual)
    
    def __iadd__(self,x):
        """
        Redefines the ``+=`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to add to our current instance.

        Returns:
            dual number: the result of the addition of the current instance and the input (dual number or scalar)
        """
        if isinstance(x, Dual):
            self.real+=x.real
            self.dual+=x.dual
            return self
        else: 
            self.real+=x
            return self

    def __truediv__(self,x):  
        """
        Redefines the ``/`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to divide our current instance with.

        Returns:
            dual number: the result of  dividing the current instance by the input (dual number or scalar).
        
        Raises:
            Warning: If division by zero is attempted.
        """
        if isinstance(x, Dual):
            if (x.real==0):
                logging.warning("Division of dual numbers is not defined when the real part of the denominator is zero")
                return np.nan
            real=self.real/x.real
            dual=(self.dual*x.real-self.real*x.dual)/(x.real**2)
            return Dual(real,dual)
        else:
            if (x==0):
                logging.warning("Division of dual numbers is not defined when the the denominator is zero")
                return np.nan
            real=self.real/x
            dual=self.dual/x
            return Dual(real,dual)
            


    def __itruediv__(self, x):
        """
        Redefines the ``/=`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to divide our current instance with.

        Returns:
            dual number: the result of  dividing the current instance by the input (dual number or scalar).
        
        Raises:
            Warning: If division by zero is attempted.
        """
        if isinstance(x, Dual):
            if (x.real == 0):
                logging.warning("Division of dual numbers is not defined when the real part of the denominator is zero")
                return np.nan
            real = self.real / x.real
            dual = (self.dual*x.real-self.real*x.dual)/(x.real**2)
            self.real=real
            self.dual=dual
            return self
        else:
            self.real/=x
            self.dual/=x
            return self


    def __sub__(self,x):
        """
        Redefines the ``-`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to subtract from our current instance.

        Returns:
            dual number: the result of the subtraction of the input (dual number or scalar) from the current instance.
        """
        if isinstance(x, Dual):
            return Dual(self.real-x.real,self.dual-x.dual)
        else:
            return Dual(self.real-x,self.dual)

    def __isub__(self,x):
        """
        Redefines the ``-=`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to subtract from our current instance.

        Returns:
            dual number: the result of the subtraction of the input (dual number or scalar) from the current instance.
        """
        if isinstance(x, Dual):
            self.real-=x.real
            self.dual-=x.dual
            return self
        else: 
            self.real-=x
            return self

    def __mul__(self,x):
        """
        Redefines the ``*`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to multiply our current instance with.

        Returns:
            dual number: the result of the multiplication between the input (dual number or scalar) and the current instance.
        """
        if isinstance(x, Dual):
            real=self.real*x.real
            dual=self.real*x.dual+self.dual*x.real
            return Dual(real,dual)
        else:
            return Dual(self.real*x,self.dual*x)
        
    def __imul__(self,x):
        """
        Redefines the ``*=`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar to multiply our current instance with.

        Returns:
            dual number: the result of the multiplication between the input (dual number or scalar) and the current instance.

        """
        if isinstance(x, Dual):
            real=self.real*x.real
            dual=self.real*x.dual+self.dual*x.real
            self.real=real
            self.dual=dual
            return self
        else:
            self.real*=x
            self.dual*=x
            return self

    
    def __pow__(self,power):
        """
        Redefines the ``**`` operator to adapt it to dual numbers.

        Parameters:
            x: the power to which we want to raise the current instance.

        Returns:
            dual number: the current instance raised to the power of the input.

        Raises:
            Warning: If the power is a dual number.
        """
        if isinstance(power, Dual):
            if(power.dual!=0):
                logging.warning("The power cant be a dual number")
                return np.nan
            else:
                real=self.real**power.real
                dual=(power.real*self.real**(power.real-1))*self.dual
                return Dual(real,dual)

        else:        
            real=self.real**power
            dual=(power*self.real**(power-1))*self.dual
            return Dual(real,dual)
    
    def __ipow__(self,power):
        """
        Redefines the ``**=`` operator to adapt it to dual numbers.

        Parameters:
            x: the power to which we want to raise the current instance.

        Returns:
            dual number: the current instance raised to the power of the input.

        Raises:
            Warning: If the power is a dual number.
        """
        if isinstance(power, Dual):
            if (power.dual!=0):
                logging.warning("The power cant be a dual number")
                return np.nan
            else:
                real=self.real**power.real
                dual=(power.real*self.real**(power.real-1))*self.dual
                self.real=real
                self.dual=dual
                return self

        else:        
            real=self.real**power
            dual=(power*self.real**(power-1))*self.dual
            self.real=real
            self.dual=dual
            return self


    def __neg__(self):
        """
        Redefines the ``-`` operator to adapt it to dual numbers.

        Returns:
            dual number: the negation of the current instance.
        """
        return Dual(-self.real,-self.dual)

    def __eq__(self,x):
        """
        Redefines the ``==`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar we want to compare the current instance to.

        Returns:
            Bool:   True if the current instance and input are equal
                    False if the current instance and input are not equal
        """
        if isinstance(x, Dual):
            return ((self.real==x.real) and (self.dual==x.dual))
        else:
            return((self.real==x) and (self.dual==0))

    def __ne__(self,x):
        """
        Redefines the ``!=`` operator to adapt it to dual numbers.

        Parameters:
            x: the dual number or scalar we want to compare the current instance to.

        Returns:
            Bool:   True if the current instance and input are not equal
                    False if the current instance and input are equal
        """       
        if isinstance(x, Dual):
            return ((self.real!=x.real) or (self.dual!=x.dual))
        else:
            return((self.real!=x) or (self.dual!=0))
        

    def __abs__(self):
        """
        Redefines the abs function to adapt it to dual numbers.

        Returns:
            dual number: the absolute value of the current instance.
        """
        return Dual(np.abs(self.real),np.abs(self.dual))

    def sin(self):
        """
        Computes the sine function of the dual number.

        Returns:
            A dual number where: 
                        the real part is the sine function of the real part of the current instance.
                        the dual part is the derivative of the sine function evaluated at the real part of the current instance multiplied with the dual part of the current instance.
        """    
        dual=self.dual*np.cos(self.real)
        return  Dual(np.sin(self.real),dual)

    def cos(self):
        """
        Computes the cosine function of the dual number.

        Returns:
            A dual number where: 
                        the real part is the cosine function of the real part of the current instance.
                        the dual part is the derivative of the cosine function evaluated at the real part of the current instance multiplied with the dual part of the current instance.
        """  
        dual=self.dual*-np.sin(self.real)
        return  Dual(np.cos(self.real),dual)

    def tan(self):
        """
        Computes the tangent function of the dual number.

        Returns:
            A dual number where: 
                        the real part is the tangent function of the real part of the current instance.
                        the dual part is the derivative of the tangent function evaluated at the real part of the current instance multiplied with the dual part of the current instance.

        Raises:
            Warning: if the cosine of the real part is 0; division by 0 is an error.
        """  
        if (np.isclose(np.cos(self.real), 0)):
            logging.warning("Tan can't be defined for this function")
            return np.nan
        dual=self.dual/(np.cos(self.real)**2)
        return  Dual(np.tan(self.real),dual)

    def log(self):
        """
        Computes the logarithm function of the dual number.

        Returns:
            A dual number where: 
                        the real part is the log of the real part of the current instance.
                        the dual part is the derivative of the log evaluated at the real part of the current instance multiplied with the dual part of the current instance.

        Raises:
            Warning: if the real part of the instance is 0; division by 0 is an error.
        """ 
        if (self.real==0):
            logging.warning("Logarithm of dual number not defined when real part is zero")
            return np.nan
        dual=(1/self.real)*self.dual
        return  Dual(np.log(self.real),dual)


    def exp(self):
        """
        Computes the exponential function of the dual number.

        Returns:
            A dual number where: 
                        the real part is the exp of the real part of the current instance.
                        the dual part is the derivative of the exp evaluated at the real part of the current instance multiplied with the dual part of the current instance.
        """  
        dual=np.exp(self.real)*self.dual
        return  Dual(np.exp(self.real),dual)


    def square(self):
        """
        Computes the square of the dual number.

        Returns:
            A dual number where: 
                        the real part is the square of the real part of the current instance.
                        the dual part is the derivative of the square function evaluated at the real part of the current instance multiplied with the dual part of the current instance.
        """  
        dual=2*self.real*self.dual
        return  Dual(np.square(self.real),dual)


    def floor(self):
        """
        Computes the floor of the dual number.

        Returns:
            A dual number where: 
                        the real part is the floor of the real part of the current instance.
                        the dual part is the floor of the dual part of the current instance.
        """  
        return  Dual(np.floor(self.real),np.floor(self.dual))


    def ceil(self):
        """
        Computes the ceil of the dual number.

        Returns:
            A dual number where: 
                        the real part is the ceil of the real part of the current instance.
                        the dual part is the ceil of the dual part of the current instance.
        """  
        return  Dual(np.ceil(self.real),np.ceil(self.dual))

    def inverse(self):
        """
        Computes the inverse of the dual number.

        Returns:
            A dual number where: 
                        the real part is the inverse of the real part of the current instance.
                        the dual part is the derivative of the inverse evaluated at the real part of the current instance multiplied with the dual part of the current instance.
        Raises:
            Warning: if the real part of the instance is 0; division by 0 is an error.
        """  
        if (self.real==0):
            logging.warning("Can't invert this Dual number")
            return np.nan
        real=1/self.real
        dual=-self.dual/(self.real**2)

        return  Dual(real,dual)


    