
#legendre polynomial
#(10) integrate(-1 --> 1)(P^2(n,x)) = (2/(2*n+1))

import numpy as np
from scipy.special import legendre
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("Enter the n: "))

def f(x):
    return (legendre(n)(x))**2

LHS=quad(f,-1,1)[0]
RHS=(2.0/(2*n+1))

print("LHS: ",LHS)
print("RHS: ",RHS)
     
    
