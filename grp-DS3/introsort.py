from math import floor, log
import time as time
import numpy as np
import sys
sys.path.append("collective")
from collective_heapsort import heapsort
from collective_quicksort import partition

def main_introsort(A):
    length = len(A)
    if (length == 0):
        return
    else:
        maxdepth = floor(log(length))*2
    introsort(A, 0, length - 1, maxdepth)

    
def introsort(A, p, r, maxdepth):
    if p >= r:
        return
    elif (maxdepth == 0):
        heapsort(A, p, r)
    else:
        q = partition(A, p, r)
        introsort(A, p, q - 1, maxdepth - 1)
        introsort(A, q + 1, r, maxdepth -1)

if __name__ == "__main__":
    n = 100
    sample_list = np.random.randint(0, 1000, n)
    print sample_list
    main_introsort(sample_list)
    print sample_list
