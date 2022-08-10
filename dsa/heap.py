#!/usr/bin/env python3

"""                 HEAP DSA
#* Heap data structure is a complete binary tree that satisfies the heap property, where any given node is
#? always greater than its child node/s and the key of the root node is the largest among all other nodes. This property is also called max heap property.
#? always smaller than the child node/s and the key of the root node is the smallest among all other nodes. This property is also called min heap property.
#* Heapify is the process of creating a heap data structure from a binary tree. It is used to create a Min-Heap or a Max-Heap.
#* https://www.programiz.com/dsa/heap-data-structure
"""

# Max-Heap data structure in Python

class Heapify:
    def __init__(self):
        self.array = []
    
    def create_heap(self, node):
        _largest_node = node
        _left_leaf = 2 * node + 1
        _right_leaf = 2 * node + 2
        
        if _left_leaf < len(self.array) and self.array[node] < self.array[_left_leaf]:
            _largest_node = _left_leaf
        
        if _right_leaf < len(self.array) and self.array[_largest_node] < self.array[_right_leaf]:
            _largest_node = _right_leaf
            
        if _largest_node != node:
            self.array[node], self.array[_largest_node] = self.array[_largest_node], self.array[node]
            self.create_heap(_largest_node)
    
    # insert data to the heap
    def insert_data(self, _):
        self.array.append(_)
        for node in range( (len(self.array) // 2) - 1, -1, -1):
            self.create_heap(node)
            
    # delete data from the heap
    def delete_data(self, _):
        _index = 0
        
        for _index in range(0, len(self.array)):
            if _ == self.array[_index]:
                break
        
        self.array[_index], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[_index]
        self.array.remove(_)
        
        for _index in range((len(self.array) // 2) - 1, -1, -1):
            self.create_heap(_index)
    
    def __repr__(self) -> str:
        return f'Heap({self.array})'

_ = Heapify()
_.insert_data(1)
_.insert_data(5)
_.insert_data(3)
_.delete_data(1)