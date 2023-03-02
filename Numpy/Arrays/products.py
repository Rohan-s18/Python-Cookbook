"""
Author: Rohan Singh
3/2/2023
Python Module to demonstrate various vector products in python using numpy
"""

#  Imports
import numpy as np
import random as rand

def create_random_array(n,min,max)->np.ndarray:
    temp = np.zeros(10)
    for i in range(0,n,1):
        temp[i] = (min+int((max-min)*rand.random()))
    return temp

#  Main function
def main():
    x = create_random_array(10,-100,100)
    y = create_random_array(10,-100,100)
    print("The vector x is: ", x)
    print("The vector y is: ", y)

    #dot-product
    print("The dot prodcuct of x and y is: ",np.dot(x,y))


if __name__ == "__main__":
    main()