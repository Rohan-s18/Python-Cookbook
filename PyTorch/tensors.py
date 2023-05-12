"""
Author: Rohan Singh
Python module to get started with Pytorch tensors
"""


#  Imports
import torch


#  Function to print tensor properties
def get_props(tensor):
    print(f'Shape of {tensor} is {tensor.shape} with dimensions {tensor.dim()}\n\n')


#  Function to change the dimensions of a tensor
def change_dim(tensor, n):
    temp = tensor.unsqueeze(n)
    return temp


#  Main Function
def main():

    one_d_tensor = torch.LongTensor([0])

    one_d_tensor_2 = torch.LongTensor([0,1,2])

    two_d_tensor = torch.LongTensor([[0,1,2],[3,4,5]])

    get_props(one_d_tensor)
    get_props(one_d_tensor_2)
    get_props(two_d_tensor)   


    #Unsqueezing tensors
    two_d_tensor_2 = change_dim(one_d_tensor_2, 0)
    two_d_tensor_3 = change_dim(one_d_tensor_2, 1) 



    get_props(two_d_tensor_2)
    get_props(two_d_tensor_3)


if __name__ == "__main__":
    main()
