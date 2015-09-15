import numpy as np


class HeapSort:

  def __init__(self, array):
    self.length = len(array) - 1 
    self.array = array

  def parent(self, i):
    return ((i-1)//2)

  def left(self, i):
    return 2*i

  def right(self, i):
    return 2*i + 1


  def max_heapify(self, i):
    left = self.left(i)
    right = self.right(i)
    if left <= self.length and self.array[left] > self.array[i]:
      largest = left
    else: 
      largest = i 
    if right <= self.length and self.array[right] > self.array[largest]:
      largest = right
    if largest != i:
      self.array[i], self.array[largest] = self.array[largest], self.array[i]
      self.max_heapify(largest)


  def build_max_heap(self):
    for i in range(self.parent(self.length + 1), -1, -1):
      self.max_heapify(i)
      

  def heapsort(self):
    self.build_max_heap()
    for i in range(self.length, 0, -1):
      self.array[0], self.array[i] = self.array[i], self.array[0]
      self.length -= 1
      self.max_heapify(0)

    return self.array


def heapsort(ar):
  heapity = HeapSort(ar)
  heapity.heapsort()


def main():
  N = 10
  ar = list(np.random.random_integers(0, 10, N))
  print heapsort(ar)
   
