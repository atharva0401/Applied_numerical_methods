# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:43:58 2021

@author: Atharva
"""
from sympy import *
import math
def taylor(function,x0,n):
    i = 0
    sum_series = 0
    while i<=n:
        sum_series+=(function.diff(x,i).subs(x,x0))/(math.factorial(i))*(x-x0)**i
        i=i+1
    return sum_series

x = Symbol('x')
print("\nInput Format:")
print("\nSine Function: sin(x)")
print("\nCosine Function: cos(x)")
print("\nTangent Function: tan(x)")
print("\nExponential Function: exp(x)")
f = eval(input("Enter the function :"))
p= eval(input("Enter the point :"))
n= eval(input("Enter the order :"))
y=simplify(taylor(f,p,n))
print("\nThe taylor series of "+str(f)+" at a = "+str(p)+" of order "+str(n)+" is \n")
pprint(y)
