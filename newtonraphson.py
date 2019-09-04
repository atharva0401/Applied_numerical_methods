# -*- coding: utf-8 -*-
"""
@author: Nitin
"""
#The program aims at solving curves using Newton-Raphson method upto 2 places of decimal
from sympy import Symbol, Derivative
x = Symbol('x')
fun = eval(input("Enter the function here: "))
der = Derivative(fun,x)
df = der.doit()
print("\nThe function you've entered is: ",fun)
print("\nThe derivative of the function is: ",df)

def value(f,a):               #function to determine value of a given function at a given point
    t = f.replace(x,a)
    return t
def dec(a,b):                 #function to compare two given numbers upto 3 places of decimal
    m = str(a-int(a))
    n = str(b - int(b))
    if m[2:5]==n[2:5]:
        return True
    else:
        return False
#iterations
print("1.Choose two points at which the value of f(x) is negative and poitive respectively\n")
print("2.Choose the mean of the  two points and enter here:\n")
x0 =eval(input())

p=True
while p==True:
    x1 = x0 - (value(fun,x0))/(value(df,x0))
    if value(df,x0)!= 0:
        if dec(x0,x1):
            print(x1," is the root of f(x)")
            p = False
        else:
            x0 = x1
    else:
        print("Your Function's derivative vanishes at x = 0")

        
    
    


    

