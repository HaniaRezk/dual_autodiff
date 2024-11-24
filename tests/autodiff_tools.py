import pytest
from dual_autodiff.dual import Dual
import numpy as np

def test_init():
    x=Dual(1.5,1.0)
    assert x.real==1.5
    assert x.dual==1.0

def test_print(capsys):
    x=Dual(1.5,1.0)
    print(x)
    captured=capsys.readouterr()
    assert "Dual(real=1.5, dual=1.0)." in captured.out

def test_add():
    x=Dual(2,1)
    y=Dual(3,2)
    z=x+y
    assert z.real==5
    assert z.dual==3

def test_iadd():
    x=Dual(2,1)
    y=Dual(7,12)
    x+=y
    assert x.real==9
    assert x.dual==13

def test_subtract():
    x=Dual(9,1)
    y=Dual(7,2)
    z=x-y
    assert z.real==2
    assert z.dual==-1

def test_isubtract():
    x=Dual(2,1.5)
    y=Dual(7,12)
    x-=y
    assert x.real==-5
    assert x.dual==-10.5

def test_multiply():
    x=Dual(2,3)
    y=Dual(4,5)
    z=x*y
    assert z.real==8
    assert z.dual==22

def test_imultiply():
    x=Dual(1.5,2)
    y=Dual(0,2.5)
    x*=y
    assert x.real==0
    assert x.dual==3.75

def test_div():
    x=Dual(0,9)
    y=Dual(4,3)
    x1=Dual(2,3)
    z=y/x
    z1=y/x1
    assert np.isnan(z)
    assert z1.real==2
    assert z1.dual==-1.5

def test_idiv():
    x=Dual(0,9)
    y=Dual(4,3)
    z=Dual(4,0)
    x1=Dual(2,3)
    y/=x
    z/=x1
    assert np.isnan(y)
    assert z.real==2
    assert z.dual==-1.5

def test_eq():
    x1=Dual(1.5,8)
    x2=Dual(1.5,8)
    assert x1==x2

def test_ne():
    y1=Dual(1,9)
    y2=Dual(1,90)
    assert y1!=y2

def test_power():
    x=Dual(6,8)
    z=x**3
    assert z.real==216
    assert z.dual==864

def test_ipower():
    x=Dual(6,8)
    x**=3
    assert x.real==216
    assert x.dual==864

def test_inverse():
    x=Dual(0,1)
    z=x.inverse()
    x1=Dual(1,5)
    z1=x1.inverse()
    assert z1.real==1
    assert z1.dual==-5
    assert np.isnan(z)

def test_sin():
    x=Dual(np.pi / 2, 1)
    y=x.sin()
    assert np.isclose(y.real, np.sin(np.pi / 2))
    assert np.isclose(y.dual, np.cos(np.pi / 2))

def test_cos():
    x=Dual(0, 1)
    y=x.cos()
    assert np.isclose(y.real, np.cos(0))
    assert np.isclose(y.dual, -np.sin(0))

def test_exp():
    x=Dual(1, 1)
    y=x.exp()
    assert np.isclose(y.real, np.exp(1))
    assert np.isclose(y.dual, np.exp(1))

def test_log():
    x=Dual(np.e, 1)
    y=x.log()
    x1=Dual(0, 1)
    y1=x1.log()
    assert np.isclose(y.real, np.log(np.e))
    assert np.isclose(y.dual, 1 / np.e)
    assert np.isnan(y1)

def test_tan():
    x=Dual(np.pi / 4, 1)
    y=x.tan()
    x1=Dual(np.pi / 2, 1)
    y1=x1.tan()
    assert np.isclose(y.real, np.tan(np.pi / 4))
    assert np.isclose(y.dual, 1 / (np.cos(np.pi / 4) ** 2))
    assert np.isnan(y1) 