"""
Author: Rohan Singh
3/3/2023
Python Module to demonstrate vector calculus in python using numpy
"""

#  Imports
import numpy as np
import random as rand


#  Function to create a random numpy array
def create_random_array(n,min,max)->np.ndarray:
    temp = np.zeros(10)
    for i in range(0,n,1):
        temp[i] = (min+int((max-min)*rand.random()))
    return temp


#  Function to create a random list
def create_random_vector(n, min, max)->list:
    temp = []
    for i in range(0,n,1):
        temp.append(min+int((max-min)*rand.random()))
    return temp


#  Main function
def main():
    pass


if __name__ == "__main__":
    main()

    