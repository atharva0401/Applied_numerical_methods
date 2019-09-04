# -*- coding: utf-8 -*-
"""
@author: Nitin
"""
'''
the following is a  simple program to generate approx. values of a given function
 at a point given by user using derivatives
 the error function being dy = df(x).dx
 This program however relies on user to provide x and dx
 '''
from sympy import Symbol, Derivative
x = Symbol('x')
fun = eval(input("Enter the function here: "))
der = Derivative(fun,x)
df = der.doit()
print("\nThe function you've entered is: ",fun)
print("\nThe derivative of the function is: ",df)
print("Step: Treat the number you have as x+dx " )
x1 = eval(input("Enter the value of x : "))
x2 = eval(input("Enter the value of dx: "))
y1 = fun.replace(x,x1)
y2 = df.replace(x,x1)
y = y1+(y2*x2)
print("The answer is: ",y)

#this code is correct upto 0.8 of error.