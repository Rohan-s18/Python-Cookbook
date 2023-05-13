"""
Author: Rohan Singh
Python Module containing source code for pre-calc
"""

#  Imports
from sympy import *
from sympy.plotting import plot3d


#  Function to plot a 3D plane
def plane(a, b):
    x, y = symbols('x y')
    z  = a*x + b*x
    plot3d(z)


#  Function to get the limit of a function
def my_limit(f, variable, b):
    y = limit(f, variable, b)
    print(y)



#  Main Function to run functions
def main():
    
    #Plotting a 3D Plane
    #plane(3,4)

    #Getting the limit of a function
    x = symbols('x')
    f = 1/x
    my_limit(f,x,oo)

    #Getting the limit (same as Euler's number)
    n = symbols('n')
    f = (1+(1/n))**n 
    my_limit(f,n,oo)


if __name__ == "__main__":
    main()

