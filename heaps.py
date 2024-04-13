import heapq
items = [20,33,42,9,4,11]
heapq.heapify(items)
print(items)

# how to remove an element in a heap list
print(heapq.heappop(items))
print(items)

# how to add an element in heap
(heapq.heappush(items,32))
print(items)