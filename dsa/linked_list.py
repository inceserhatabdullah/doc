#!/usr/bin/env python3

"""LINKED LIST
# * A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node
# ? You have to start somewhere, so we give the address of the first node a special name called HEAD
# ? Also, the last node in the linked list can be identified because its next portion points to NULL.
# ? Traversal: access each element of the linked list
# ? Insertion: adds a new element to the linked list
# ? Deletion: removes the existing elements
# ? Search: find a node in the linked list
# ? Sort: sort the nodes of the linked list
# * https://www.programiz.com/dsa/linked-list
"""

# Linked list implementation in Python

class Node:
    def __init__(self, _):
        self._ = _
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, _):
        _ = Node(_)
        _.next = self.head
        self.head = _
    
    def insert_after(self, _prev, _):
        if _prev is None:
            return False
        
        _ = Node(_)
        _.next = _prev.next
        _prev.next = _
        
    def insert_end(self, _):
        _ = Node(_)
        
        if self.head is None:
            self.head = _
            return
        
        _last = self.head
        
        while _last.next:
            _last = _last.next
        
        _last.next = _
    
    # Deleting a node    
    def delete_node(self, node):
        if self.head is None:
            return False
        
        _temporary = self.head
        
        if node == 0:
            self.head = _temporary
            _temporary = None
            return True
        
        # Find the key to be deleted
        for _iterator in range(node - 1):
            _temporary = _temporary.next
            if _temporary is None:
                break
            
        if _temporary is None:
            return False
        
        if _temporary.next is None:
            return False
        
        _next = _temporary.next.next
        _temporary.next = None
        _temporary.next = _next
        
        
    # search an element    
    def search_nodes(self, node):
        _current = self.head
        
        while _current is not None:
            if _current._ == node:
                return True
            _current = _current.next
            
        return False
    
    # sort the linked list
    def sort_linked_list(self):
        _current = self.head
        _temporary = Node(None)
        
        if self.head is None:
            return False
        
        while _current is not None:
            _temporary = _current.next
            
            while _temporary is not None:
                if _current._ > _temporary._:
                    _current._, _temporary._ = _temporary._, _current._
                    
                _temporary = _temporary.next
            _current = _current.next
            
           
    
_list = LinkedList()
_list.head = Node("First")

# Connect to node
_list.head.next = Node("Next")
_list.insert_at_beginning("Insert at beginning")
_list.insert_after(_list.head.next, "Insert after")
_list.insert_end("Insert end")
#_list.delete_node(2)
_list.search_nodes("Next")
_list.sort_linked_list()
while _list.head != None:
    print(f'{_list.head._}')
    _list.head = _list.head.next