from math import floor, log
import time as time
import numpy as np
import sys
sys.path.append("collective")
from collective_heapsort import heapsort

def partition(A, p, r):
    """Returns a partition point.
    Implemented with a for loop."""
    i = p - 1
    for j in range(p, r):
        if A[j] < A[r]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r],  A[i + 1]
    return i + 1

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




# class HeapSort:

#   def __init__(self, array, start, last):
#     self.length = last - start + 1 
#     self.array = array
#     self.start = start
#     self.last = last

#   def parent(self, i):
#     return (((i-self.start))//2) + self.start

#   def left(self, i):
#     return 2*(i-self.start) + self.start

#   def right(self, i):
#     return 2*(i-self.start) + 1 + self.start

#   def swap(self, i, j):
#     self.array[i], self.array[j] = self.array[j], self.array[i]


#   def max_heapify(self, i):
#     left = self.left(i)
#     right = self.right(i)
#     if left <= self.last and self.array[left] > self.array[i]:
#       largest = left
#     else: 
#       largest = i 
#     if right <= self.last and self.array[right] > self.array[largest]:
#       largest = right
#     if largest != i:
#       self.swap(i, largest)
#       self.max_heapify(largest)


#   def build_max_heap(self):
#     for i in range(self.parent(self.last), self.start-1, -1):
#       self.max_heapify(i)
      

#   def heapsort(self):
#     self.build_max_heap()
#     for i in range(self.last, self.start, -1):
#       self.array[self.start], self.array[i] = self.array[i], self.array[self.start]
#       self.last -= 1
#       self.max_heapify(self.start)

#     return self.array


# def heapsort(ar, start = 0, last = False):
#   if not last:
#     last = len(ar) - 1
#   HeapSort(ar, start, last).heapsort()


if __name__ == "__main__":
    n = 100
    sample_list = np.random.randint(0, 1000, n)
    print sample_list
    main_introsort(sample_list)
    print sample_list
