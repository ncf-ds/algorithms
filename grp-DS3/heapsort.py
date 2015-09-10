class HeapSort:

  def __init__(self, array):
    self.length = len(array) - 1 
    self.array = array

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
    for i in range(self.length/2 - 1, 0, -1):
      self.max_heapify(i)
      

  def heapsort(self):
    self.build_max_heap()
    for i in range(self.length, 0, -1):
      self.array[0], self.array[i] = self.array[i], self.array[0]
      self.length -= 1
      self.max_heapify(0)
    return self.array


def main():
  ar = [9, 3, 4, 8, 5, 1, 6, 7, 2, 0]
  heapity = HeapSort(ar)
  print heapity.heapsort()


main()