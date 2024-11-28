# tests/autodiff_tools.py
import pytest
from dual_autodiff.dual import Dual
import numpy as np

def test_init():
    """
    A test that makes sure that our Dual class initializes correctly.

    """
    x=Dual(1.5,1.0)
    assert x.real==1.5
    assert x.dual==1.0

def test_print(capsys):
    """
    A test that makes sure that print(Dual(_,_)) outputs "Dual(real=_, dual=_).".

    """
    x=Dual(1.5,1.0)
    print(x)
    captured=capsys.readouterr()
    assert "Dual(real=1.5, dual=1.0)." in captured.out

def test_add():
    """
    A test that makes sure that the operator ``+`` correctly adds dual numbers.

    """
    x=Dual(2,1)
    y=Dual(3,2)
    z=x+y
    assert z.real==5
    assert z.dual==3

def test_add_scalar():
    """
    A test that makes sure that the operator ``+`` correctly adds a dual number and a scalar.

    """
    x=Dual(2,1)
    z=x+5
    assert z.real==7
    assert z.dual==1

def test_iadd():
    """
    A test that makes sure that the operator ``+=`` correctly adds a dual number to another dual number.

    """
    x=Dual(2,1)
    y=Dual(7,12)
    x+=y
    assert x.real==9
    assert x.dual==13

def test_iadd_scalar():
    """
    A test that makes sure that the operator ``+=`` correctly adds a scalar to a dual number.

    """
    y=Dual(7,12)
    y+=2
    assert y.real==9
    assert y.dual==12


def test_radd_scalar():
    """
    A test that makes sure that the reverse operator ``+`` correctly adds a scalar to a dual number.

    """
    x=Dual(7,12)
    y=2+x
    assert y.real==9
    assert y.dual==12

def test_subtract():
    """
    A test that makes sure that the operator ``-`` correctly subtracts dual numbers.

    """
    x=Dual(9,1)
    y=Dual(7,2)
    z=x-y
    assert z.real==2
    assert z.dual==-1

def test_subtract_scalar():
    """
    A test that makes sure that the operator ``-`` correctly subtracts a scalar from a dual number.

    """
    x=Dual(9,1)
    z=x-7
    assert z.real==2
    assert z.dual==1

def test_isubtract():
    """
    A test that makes sure that the operator ``-=`` correctly subtracts a dual number from another dual number.

    """
    x=Dual(2,1.5)
    y=Dual(7,12)
    x-=y
    y-=2
    assert x.real==-5
    assert x.dual==-10.5
    assert y.real==5
    assert y.dual==12

def test_isubtract_scalar():
    """
    A test that makes sure that the operator ``-=`` correctly subtracts a scalar from a dual number.

    """
    y=Dual(7,12)
    y-=2
    assert y.real==5
    assert y.dual==12


def test_rsub_scalar():
    """
    A test that makes sure that the reverse operator ``-`` correctly subtracts a dual number from a scalar.

    """
    x=Dual(7,12)
    y=2-x
    assert y.real==-5
    assert y.dual==-12

def test_multiply():
    """
    A test that makes sure that the operator ``*`` correctly multiplies two dual numbers.

    """
    x=Dual(2,3)
    y=Dual(4,5)
    z=x*y
    assert z.real==8
    assert z.dual==22

def test_multiply_scalar():
    """
    A test that makes sure that the operator ``*`` correctly multiplies a dual number and a scalar.

    """
    x=Dual(2,3)
    z=x*10
    assert z.real==20
    assert z.dual==30

def test_imultiply():
    """
    A test that makes sure that the operator ``*=`` correctly multiplies two dual numbers.

    """
    x=Dual(1.5,2)
    y=Dual(0,2.5)
    x*=y
    assert x.real==0
    assert x.dual==3.75

def test_imultiply_scalar():
    """
    A test that makes sure that the operator ``*=`` correctly multiplies a dual number and a scalar.

    """
    y=Dual(0,2.5)
    y*=10
    assert y.real==0
    assert y.dual==25

def test_rmul_scalar():
    """
    A test that makes sure that the reverse operator ``*`` correctly multiplies a dual number and a scalar.

    """
    x=Dual(7,12)
    y=2*x
    assert y.real==14
    assert y.dual==24

def test_div():
    """
    A test that makes sure that the operator ``/`` correctly divides a dual number by another dual number and handles invalid input cases.

    """
    x=Dual(0,9)
    y=Dual(4,3)
    x1=Dual(2,3)
    z=y/x
    z1=y/x1
    assert np.isnan(z)
    assert z1.real==2
    assert z1.dual==-1.5

def test_div_scalar():
    """
    A test that makes sure that the operator ``/`` correctly divides a dual number by a scalar and handles invalid input cases.

    """
    x=Dual(2,3)
    z=x/2
    y=x/0
    assert z.real==1
    assert z.dual==1.5
    assert np.isnan(y)

def test_idiv():
    """
    A test that makes sure that the operator ``/=`` correctly divides a dual number by another dual number and handles invalid input cases.

    """
    y=Dual(4,3)
    z=Dual(4,3)
    x=Dual(0,9)
    x1=Dual(2,3)
    y/=x
    z/=x1
    assert np.isnan(y)
    assert z.real==2
    assert z.dual==-1.5

def test_idiv_scalar():
    """
    A test that makes sure that the operator ``/=`` correctly divides a dual number by a scalar and handles invalid input cases.

    """
    x=Dual(2,3)
    x/=2
    assert x.real==1
    assert x.dual==1.5

def test_rdiv_scalar():
    """
    A test that makes sure that the reverse operator ``/`` correctly divides a scalar by a dual number.

    """
    x=Dual(7,12)
    x1=Dual(0,10)
    y=2/x
    z=2/x1
    assert y.real==(2/7)
    assert y.dual==(-24/49)
    assert np.isnan(z)

def test_eq():
    """
    A test that makes sure that the operator ``==`` correctly identifies when two dual numbers are equal.

    """
    x=Dual(1.5,8)
    y=Dual(1.5,8)
    z=Dual(1.5001,8)
    assert y==x
    assert not(z==x)

def test_eq_scalar():
    """
    A test that makes sure that the operator ``==`` correctly identifies when a scalar is be equal to a dual number.

    """
    y=4
    x=Dual(4,0)
    x1=Dual(4,0.001)
    assert y==x
    assert not (y==x1)

def test_ne():
    """
    A test that makes sure that the operator ``==`` correctly differentiates between two different dual numbers.

    """
    x=Dual(1,9)
    y=Dual(1,90)
    y1=Dual(1,9)
    assert x!=y
    assert not (x!=y1)

def test_ne_scalar():
    """
    A test that makes sure that the operator ``==`` correctly differentiates between a dual number and a scalar.

    """
    x=Dual(4,1)
    y=Dual(4,0)
    assert x!=4
    assert not (y!=4)

def test_ge():
    """
    A test that makes sure that the operator ``>=`` behaves according to its redefinition.

    """
    x=Dual(1,9)
    y=Dual(2,90)
    assert y>=x
    assert y>=2
    assert 7>=y
    assert not(x>4)

def test_gt():
    """
    A test that makes sure that the operator ``>`` behaves according to its redefinition.

    """
    x=Dual(1,9)
    y=Dual(2,90)
    assert y>x
    assert not(y>2)
    assert 8>y

def test_lt():
    """
    A test that makes sure that the operator ``<`` behaves according to its redefinition.

    """
    x=Dual(1,9)
    y=Dual(2,90)
    assert x<y
    assert 0<x
    assert x<5
    assert not(1<x)

def test_le():
    """
    A test that makes sure that the operator ``<=`` behaves according to its redefinition.

    """
    x=Dual(1,9)
    y=Dual(2,90)
    assert x<=y
    assert 1<=y
    assert not(y<=0)

def test_power():
    """
    A test that makes sure that the operator ``**`` behaves accordingly and handles invalid input cases.

    """
    x=Dual(6,8)
    y=Dual(7,8)
    z=x**3
    z1=x**y
    assert z.real==216
    assert z.dual==864
    assert np.isnan(z1)

def test_power_scalar():
    """
    A test that makes sure that the operator ``**`` behaves accordingly when the power is a dual number with no dual part.

    """
    x=Dual(6,8)
    y=Dual(3,0)
    z=x**y
    assert z.real==216
    assert z.dual==864

def test_ipower():
    """
    A test that makes sure that the operator ``**=`` behaves accordingly when the power is a scalar.

    """
    x=Dual(6,8)
    y=Dual(6,8)
    z=Dual(6,8)
    x**=3
    z**=y
    assert x.real==216
    assert x.dual==864
    assert np.isnan(z)

def test_ipower_scalar():
    """
    A test that makes sure that the operator ``**=`` behaves accordingly when the power is a dual number with no dual part.

    """
    x=Dual(6,8)
    y=Dual(3,0)
    x**=y
    assert x.real==216
    assert x.dual==864

def test_inverse():
    """
    A test that makes sure that the inverse() function behaves accordingly and handles invalid input cases.

    """
    x=Dual(0,1)
    z=x.inverse()
    x1=Dual(1,5)
    z1=x1.inverse()
    assert z1.real==1
    assert z1.dual==-5
    assert np.isnan(z)

def test_sin():
    """
    A test that makes sure that the sin() function behaves accordingly.

    """
    x=Dual(np.pi / 2, 1)
    y=x.sin()
    assert np.isclose(y.real, np.sin(np.pi / 2))
    assert np.isclose(y.dual, np.cos(np.pi / 2))

def test_cos():
    """
    A test that makes sure that the cos() function behaves accordingly.

    """
    x=Dual(0, 1)
    y=x.cos()
    assert np.isclose(y.real, np.cos(0))
    assert np.isclose(y.dual, -np.sin(0))

def test_exp():
    """
    A test that makes sure that the exp() function behaves accordingly.

    """
    x=Dual(1, 1)
    y=x.exp()
    assert np.isclose(y.real, np.exp(1))
    assert np.isclose(y.dual, np.exp(1))

def test_log():
    """
    A test that makes sure that the log() function behaves accordingly and handles invalid input cases.

    """
    x=Dual(np.e, 1)
    y=x.log()
    x1=Dual(0, 1)
    y1=x1.log()
    assert np.isclose(y.real, np.log(np.e))
    assert np.isclose(y.dual, 1 / np.e)
    assert np.isnan(y1)

def test_tan():
    """
    A test that makes sure that the tan() function behaves accordingly and handles invalid input cases.

    """
    x=Dual(np.pi / 4, 1)
    y=x.tan()
    x1=Dual(np.pi / 2, 1)
    y1=x1.tan()
    assert np.isclose(y.real, np.tan(np.pi / 4))
    assert np.isclose(y.dual, 1 / (np.cos(np.pi / 4) ** 2))
    assert np.isnan(y1) 