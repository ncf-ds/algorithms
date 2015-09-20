import numpy as np
import time
import matplotlib.pyplot as pl
import copy

class HeapSort:

  def __init__(self, array, start, last):
    self.length = last - start + 1 
    self.array = array
    self.start = start
    self.last = last

  def parent(self, i):
    return (((i-self.start)-1)//2) + self.start

  def left(self, i):
    return 2*(i-self.start) + self.start

  def right(self, i):
    return 2*(i-self.start) + 1 + self.start

  def swap(self, i, j):
    self.array[i], self.array[j] = self.array[j], self.array[i]


  def max_heapify(self, i):
    left = self.left(i)
    right = self.right(i)
    if left <= self.last and self.array[left] > self.array[i]:
      largest = left
    else: 
      largest = i 
    if right <= self.last and self.array[right] > self.array[largest]:
      largest = right
    if largest != i:
      self.swap(i, largest)
      self.max_heapify(largest)


  def build_max_heap(self):
    for i in range(self.parent(self.last), self.start-1, -1):
      self.max_heapify(i)
      

  def heapsort(self):
    self.build_max_heap()
    for i in range(self.last, self.start, -1):
      self.array[self.start], self.array[i] = self.array[i], self.array[self.start]
      self.last -= 1
      self.max_heapify(self.start)

    return self.array


def heapsort(ar, start = 0, last = False):
  if not last:
    last = len(ar) - 1
  HeapSort(ar, start, last).heapsort()


# def main():
#   N = 10
#   ar = list(np.random.random_integers(0, 10, N))
#   print heapsort(ar)
   

if __name__ == "__main__":
  # sample_list = [10,9,31,9,8]
  # print "Original list: {}".format(sample_list)     
  # running_time_upheap = HeapSort(sample_list).sort_my_list_up_heap() 
  # running_time_downheap  = HeapSort(sample_list).sort_my_list()     
  # print "Sorted list: {}".format(sample_list)
  # print "downheap {}sec".format(running_time_downheap)
  # print "upheap {}sec".format(running_time_upheap)
  
  # x= []
  # y,y1= [],[]
  # for n in range(0,15001,1000):
  #   sample_list = np.random.randint(-1000, 1000, n)
  #   start = time.clock()
  #   heapsort(sample_list)
  #   # running_time_upheap = HeapSort(sample_list).sort_my_list()
  #   end = time.clock()
  #   running_time_downheap = (end - start)
  #   print "N = {} : downheap {} sec".format(n,running_time_downheap)
  #   # print "N = {} : upheap {} sec".format(n,running_time_upheap)
 
  #   x.append(n)
  #   y.append(running_time_downheap)
  #   # y1.append(running_time_upheap)
      
  # # create and show a plot
  # pl.plot(x,y,'o')
  # # pl.plot(x,y1,'--')
  # pl.title("Heap Sort")
  # pl.xlabel('N')
  # pl.ylabel('Running Time')
  # pl.show()
 

  a = list(np.random.randint(-1000,1000,10))
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