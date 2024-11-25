import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class Dual:
    def __init__(self,real,dual):
        self.real=real
        self.dual=dual

    
    #Redefining the __str__ method to get the desired print format
    def __str__(self):
        string="Dual(real="+ str(self.real) +", dual="+ str(self.dual)+ ")."
        return string

    #Redefining the basic arithmetic operations
    def __add__(self,x):
        if isinstance(x, Dual):
            return Dual(x.real+self.real,x.dual+self.dual)
        else:
            return Dual(x + self.real,self.dual)
    
    def __iadd__(self,x):
        if isinstance(x, Dual):
            self.real+=x.real
            self.dual+=x.dual
            return self
        else: 
            self.real+=x
            return self

    def __truediv__(self,x):
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
        if isinstance(x, Dual):
            return Dual(self.real-x.real,self.dual-x.dual)
        else:
            return Dual(self.real-x,self.dual)

    def __isub__(self,x):
        if isinstance(x, Dual):
            self.real-=x.real
            self.dual-=x.dual
            return self
        else: 
            self.real-=x
            return self

    def __mul__(self,x):
        if isinstance(x, Dual):
            real=self.real*x.real
            dual=self.real*x.dual+self.dual*x.real
            return Dual(real,dual)
        else:
            return Dual(self.real*x,self.dual*x)
        
    def __imul__(self,x):
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
        return Dual(-self.real,-self.dual)

    def __eq__(self,x):
        if isinstance(x, Dual):
            return ((self.real==x.real) and (self.dual==x.dual))
        else:
            return((self.real==x) and (self.dual==0))

    def __ne__(self,x):
        if isinstance(x, Dual):
            return ((self.real!=x.real) or (self.dual!=x.dual))
        else:
            return((self.real!=x) or (self.dual!=0))
        

    def __abs__(self):
        return Dual(np.abs(self.real),np.abs(self.dual))

    #Defining other essential functions (details in the project report)
    def sin(self):
        dual=self.dual*np.cos(self.real)
        return  Dual(np.sin(self.real),dual)

    def cos(self):
        dual=self.dual*-np.sin(self.real)
        return  Dual(np.cos(self.real),dual)

    def tan(self):
        if (np.isclose(np.cos(self.real), 0)):
            logging.warning("Tan can't be defined for this function")
            return np.nan
        dual=self.dual/(np.cos(self.real)**2)
        return  Dual(np.tan(self.real),dual)

    def log(self):
        if (self.real==0):
            logging.warning("Logarithm of dual number not defined when real part is zero")
            return np.nan
        dual=(1/self.real)*self.dual
        return  Dual(np.log(self.real),dual)


    def exp(self):
        dual=np.exp(self.real)*self.dual
        return  Dual(np.exp(self.real),dual)


    def square(self):
        dual=2*self.real*self.dual
        return  Dual(np.square(self.real),dual)


    def floor(self):
        return  Dual(np.floor(self.real),np.floor(self.dual))


    def ceil(self):
        return  Dual(np.ceil(self.real),np.ceil(self.dual))

    def inverse(self):
        if (self.real==0):
            logging.warning("Can't invert this Dual number")
            return np.nan
        real=1/self.real
        dual=-self.dual/(self.real**2)

        return  Dual(real,dual)


    