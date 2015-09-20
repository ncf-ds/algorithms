"""
Committee: Tanner, Carlos, Jacopo, Nathan, Shahab
"""

import time
import numpy.random as nprnd
import matplotlib.pyplot as pl
import copy

class HSFun(object):

    def MaxHeapify(self,A,i):
        #left child of i
        l = 2*(i - self.start) + self.start
        #right child of i
        r = 2*(i - self.start + 1) + self.start
        if (l < self.end and A[l] > A[i]):
            largest = l
        else:
            largest = i
        if (r < self.end and A[r] > A[largest]):
            largest = r
        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            self.MaxHeapify(A,largest)
            
            
    def BuildMaxHeap(self,A):
        for i in range(((self.end - self.start)//2 - 1) + self.start, (self.start-1), -1):
            self.MaxHeapify(A,i)
     
     
            
    def HeapSort(self,A):
        self.BuildMaxHeap(A)
        for i in range((self.end-1), self.start, -1):
            A[self.start], A[i] = A[i], A[self.start]
            self.end -= 1
            self.MaxHeapify(A, self.start)


    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = end - start


def heapsort(ar, start = 0, end = False):
    
    if not end:
        end = len(ar)

    HeapSortCall = HSFun(start, end)
    HeapSortCall.HeapSort(ar)


if __name__ == "__main__":

    a = list(nprnd.randint(-1000,1000,10))
    b = copy.copy(a)
    c = copy.copy(b)

    print(a)
    heapsort(a, 3)
    print(a)
    print(b)
    temp = b[3:]
    heapsort(temp, 0)
    b[3:] = temp
    print(b)


    print(a==b)
    # x= []
    # y,y1= [],[]
    # for n in range(0,15001,1000):
    #     sample_list = nprnd.randint(-1000, 1000, n)
    #     start = time.clock()
    #     heapsort(sample_list)
    #     end = time.clock()
    #     running_time_downheap = end - start
    #     print "N = {} : {}sec".format(n,running_time_downheap)
 
    #     x.append(n)
    #     y.append(running_time_downheap)
          
    # # create and show a plot
    # pl.plot(x,y)
    # pl.title("Heap Sort")
    # pl.xlabel('N')
    # pl.ylabel('Running Time')
    # pl.show()
 
