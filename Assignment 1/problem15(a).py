from sympy import *
s = symbols('s') 

#Numerator N(s) of G(s)
N = 45*(s**2 + 37*s + 74)*(s**3 + 28*s**2 +32*s + 16) 
N_e = expand(N)

#Denominator D(s) of G(s)
D = (s + 39)*(s + 47)*(s**2 + 2*s + 100)*(s**3 + 27*s**2 + 18*s + 15)
D_e = expand(D)

#Printing given transfer function G(s) and it's polynomial form
G = N/D
print("\n Given Transfer function G(s) = {}".format(G)) 

G_poly = expand(N)/expand(D)
print("\n Polynomial form of G(s) = {}".format(G_poly)) 
  
#Solving poles and zeroes using np.roots() method 
import numpy as np

N = np.poly1d([45,2925,51390,147240,133200,53280])
zeroes = np.roots(N)
print("\n Zeroes of G(s) = ",zeroes)

D = np.poly1d([1,115,4499,70700,553692,5201463,3483390,2749500])
Poles = np.roots(D)
print("\n Poles of G(s) = ",Poles)
