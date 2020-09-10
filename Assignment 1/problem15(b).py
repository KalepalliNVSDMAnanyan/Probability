from sympy import *
s = symbols('s') 

#Numerator N(s) of G(s)
N = 56*(s + 14)*(s**3 + 49*s**2 +62*s + 53) 
N_e = expand(N)

#Denominator D(s) of G(s)
D = (s**3 + 81*s**2 + 76*s + 65)*(s**2 + 88*s + 33)*(s**2 + 56*s + 77)
D_e = expand(D)

#Printing given transfer function G(s) and it's polynomial form
G = N/D
print("\n Given Transfer function G(s) = {}".format(G)) 

G_poly = expand(N)/expand(D)
print("\n Polynomial form of G(s) = {}".format(G_poly)) 
  
#Solving poles and zeroes using np.roots() method 
import numpy as np

N = np.poly1d([56,3528,41888,51576,41552])
zeroes = np.roots(N)
print("\n Zeroes of G(s) = ",zeroes)

D = np.poly1d([1,225,16778,427711,1093333,1188715,753676,165165])
Poles = np.roots(D)
print("\n Poles of G(s) = ",Poles)
