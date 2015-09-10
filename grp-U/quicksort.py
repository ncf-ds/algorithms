# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:26:56 2015
QuickSort - as based off of the psuedocode from
http://www.algorithmist.com/index.php/Quicksort#Pseudocode
@author: David Duffrin
"""

def QuickSort(sortMe):
    QuickSortRecurs(sortMe, 0, len(sortMe))

def QuickSortRecurs(sortMe, low, high):
    if (low < high):
        pivot = QuickSortPart(sortMe, low, high)
        QuickSortRecurs(sortMe, low, pivot - 1)
        QuickSortRecurs(sortMe, pivot + 1, high)

def QuickSortPart(sortMe, low, high):
    pivot = sortMe[low]
    left = low
    for i in range(low+1, high):
        if (sortMe[i] < pivot):
            left = left + 1
            sortMe[i], sortMe[left] = sortMe[left], sortMe[i]
    sortMe[low], sortMe[left] = sortMe[left], sortMe[low]
    return left
    
sortMe = [54,26,93,17,77,31,44,55,20]
print(sortMe)
QuickSort(sortMe)
print(sortMe)