"""
Author: Rohan Singh
3/8/2023
This Python Module contains substance retrieval using PubChemPy
"""

#  Imports
from pubchempy import *


#  Main function for demonstration
def main():
    
    #  Retrieving from CID/SID
    print(get_compounds(1234))
    print(get_substances(4321))

    #Retrieving using name
    get_compounds('Aspirin', 'name')

    #Retrieving using smiles
    print(get_compounds('C1=CC2=C(C3=C(C=CC=N3)C=C2)N=C1', 'smiles'))

    #Getting 3d record type
    print(get_compounds('Aspirin', 'name', record_type='3d'))





if __name__ == "__main__":
    main()