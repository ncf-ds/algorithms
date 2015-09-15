"""
@author:Shahab
@version: 1.0
Group: John, Becky, Shahab
Committee: Tanner, Carlos, Jacopo, Nathan, Shahab
"""
import time
import numpy.random as nprnd
import matplotlib.pyplot as pl #plotting api

class HeapSort():
    def __init__(self,mylist):
        self.input_list = mylist
       
    def find_parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return 2*i + 1
    
    def right(self,i):
         return 2*i + 2
    
    def has_left(self,i):
        return self.left(i) < len(self.input_list)
    
    def has_right(self,i):
        return self.right(i) < len(self.input_list)
    
    def swap(self,i,j):
        self.input_list[i],self.input_list[j] = self.input_list[j],self.input_list[i]
    
    def down_heap(self,i,size):
        if self.has_left(i) and self.left(i)<= size:
            greater_node_index = self.left(i) # left or right doesn't matter here
            if self.has_right(i) and self.right(i)<= size:
                if self.input_list[self.right(i)]>self.input_list[self.left(i)]:
                    greater_node_index = self.right(i)
            if self.input_list[greater_node_index] > self.input_list[i]:
                self.swap(i, greater_node_index)
                self.down_heap(greater_node_index,size)
    
    def heapify(self,end):
        last_parent = self.find_parent(end)  
        for i in range(last_parent,-1,-1):
            self.down_heap(i,end)   
    
    def sort_my_list(self):
        start = time.time()
        N = len(self.input_list)
        for end in range(N-1,-1,-1):
            self.heapify(end)
            self.swap(0,end)
        end  = time.time()
        return end - start


if __name__ == "__main__":
    sample_list = [4,6,1,7,2]
    print "Original list: {}".format(sample_list)     
    HeapSort(sample_list).sort_my_list()        
    print "Sorted list: {}".format(sample_list)
    
    x= []
    y= []
    for n in range(0,1001,40):
        sample_list = nprnd.randint(-1000, 1000, n)
        running_time = HeapSort(sample_list).sort_my_list()
        print "N = {} : {}sec".format(n,running_time)
        x.append(n)
        y.append(running_time)
        
    # create and show a plot
    pl.plot(x,y,'o')
    pl.title("Heap Sort")
    pl.xlabel('N')
    pl.ylabel('Running Time')
    pl.show()
 
