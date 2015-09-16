"""
@author:Shahab
@version: 1.2
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
    
    def up_heap(self,i,end):
        p = self.find_parent(i)
        if i>=0 and i<=end and self.input_list[i] > self.input_list[p]:
            self.swap(i, p)
            self.up_heap(p, end)
    
    def heapify(self,end):
        last_parent = self.find_parent(end)  
        for i in range(last_parent,-1,-1):
            self.down_heap(i,end)   
    
    def up_heapify(self, end):
        for i in range(end+1):
            self.up_heap(i, end)
        
    def sort_my_list(self):
        start = time.clock()
        N = len(self.input_list)
        for end in range(N-1,-1,-1):
            self.heapify(end)
            self.swap(0,end)
        end  = time.clock()
        return end - start
    
    def sort_my_list_up_heap(self):
        start = time.clock()
        N = len(self.input_list)
        for end in range(N-1,-1,-1):
            self.up_heapify(end)
            self.swap(0,end)
        end  = time.clock()
        return end - start


if __name__ == "__main__":
    sample_list = [10,9,31,9,8]
    print "Original list: {}".format(sample_list)     
    running_time_upheap = HeapSort(sample_list).sort_my_list_up_heap() 
    running_time_downheap  = HeapSort(sample_list).sort_my_list()     
    print "Sorted list: {}".format(sample_list)
    print "downheap {}sec".format(running_time_downheap)
    print "upheap {}sec".format(running_time_upheap)
    
    x= []
    y,y1= [],[]
    for n in range(0,1501,100):
        sample_list = nprnd.randint(-1000, 1000, n)
        running_time_upheap = HeapSort(sample_list).sort_my_list_up_heap()
        running_time_downheap = HeapSort(sample_list).sort_my_list()
        print "N = {} : downheap {}sec".format(n,running_time_downheap)
        print "N = {} : upheap {}sec".format(n,running_time_upheap)
 
        x.append(n)
        y.append(running_time_downheap)
        y1.append(running_time_upheap)
          
    # create and show a plot
    pl.plot(x,y,'o')
    pl.plot(x,y1,'--')
    pl.title("Heap Sort")
    pl.xlabel('N')
    pl.ylabel('Running Time')
    pl.show()
 
