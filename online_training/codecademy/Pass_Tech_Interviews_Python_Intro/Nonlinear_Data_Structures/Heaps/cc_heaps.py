# import random number generator
from random import randrange
# import heap class
from cc_heaps_class import MinHeap

# make an instance of MinHeap
min_heap = MinHeap()

# populate min_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
    min_heap.add(el)

min_heap.add(1)
# remove minimum until min_heap is empty
# while min_heap.count != 0:
#     min_heap.retrieve_min()


### TESTING GROUNDS
my_min_heap = MinHeap()
my_min_heap.add(10)
my_min_heap.add(13)
my_min_heap.add(21)
my_min_heap.add(61)
my_min_heap.add(22)
my_min_heap.add(23)
my_min_heap.add(99)
print("My Min Heap List: \n", my_min_heap.heap_list)
# my_min_heap.add(12)
# my_min_heap.add(1)

while len(my_min_heap.heap_list) != 1:
    print(my_min_heap.heap_list)
    my_min_heap.retrieve_min()
