"""
Author: Rohan Singh
3/8/2023
This Python Module contains property retrieval using PubChemPy
"""

#  Imports
from pubchempy import *


#  Main function for demonstration
def main():
    
    #  Initializing a compound object
    c = Compound.from_cid(6819)
    print(c)
    print("\n")

    #  Prinitng the attributes of the compound c
    r = c.record
    for rec in r:
        print(rec)
    print("\n")

    print("Printing the properties")
    #  Retriving the properties without having to create a compound
    p = get_properties('IsomericSMILES', 'CC', 'smiles', searchtype='superstructure')
    for prop in p:
        print(prop)
    print("\n")




if __name__ == "__main__":
    main()