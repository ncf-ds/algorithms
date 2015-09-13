# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:49:50 2015

@author: CW
"""
import numpy as np


def MergeSort(A):
    
    if len(A)>1:
        mid = len(A)//2
        
        left_side = A[:mid]
        right_side = A[mid:]
        
        leftL = len(left_side)
        rightL = len(right_side)
       
        MergeSort(left_side)
        MergeSort(right_side)
        
        i=j=k=0
        
        while i<leftL and j < rightL:
            if left_side[i] < right_side[j]:
                A[k] = left_side[i]
                i = i+1
            else:
                A[k] = right_side[j]
                j=j+1
            k = k+1
        
        while i < leftL:
            A[k] = left_side[i]
            i=i+1
            k=k+1
        
        while j < rightL:
            A[k] = right_side[j]
            j=j+1
            k=k+1
        
def main():
    N = 10
    A = list(np.random.random_integers(0, 10, N))
    print("Before:" + str(A))
    MergeSort(A)
    print("After:" + str(A))
