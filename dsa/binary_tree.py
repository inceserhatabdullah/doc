#!/usr/bin/env python3

# Binary Tree in Python

"""                 BINARY TREE
#* A binary tree is a tree data structure in which each parent node can have at most two children. Each node of a binary tree consists of three items:
#? data item
#? address of left child
#? address of right child

trees(node to left): 1(root) 12(first left node) 9(first right node) 5(first left node's left leaf) 6(first left node's right leaf)
INORDER TRAVERSAL
#? First, visit all the nodes in the left subtree
#? Then the root node
#? Visit all the nodes in the right subtree
#! 5 --> 12 --> 6 --> 1 --> 9

PREORDER TRAVERSAL
#? Visit root node
#? Visit all the nodes in the left subtree
#? Visit all the nodes in the right subtree
#! 1 --> 12 --> 5 --> 6 --> 9

POSTORDER TRAVERSAL
#? Visit all the nodes in the left subtree
#? Visit all the nodes in the right subtree
#? Visit the root node
#! 5 --> 6 --> 12 --> 9 --> 1  

                    FULL BINARY TREE
#* A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.
#? It is also known as a proper binary tree.

Let, i = the number of internal nodes
       n = be the total number of nodes
       l = number of leaves
      λ = number of levels

#? The number of leaves is i + 1.
#? The total number of nodes is 2i + 1.
#? The number of internal nodes is (n – 1) / 2.
#? The number of leaves is (n + 1) / 2.
#? The total number of nodes is 2l – 1.
#? The number of internal nodes is l – 1.
#? The number of leaves is at most 2λ - 1.

                    PERFECT BINARY TREE
#* A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

                    COMPLETE BINARY TREE
#* A complete binary tree is just like a full binary tree, but with two major differences
#? Every level must be completely filled
#? All the leaf elements must lean towards the left.
#? The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

                    DEGENERATE BINARY TREE
#* A degenerate or pathological tree is the tree having a single child either left or right.

                    SKEWED BINARY TREE
#* A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes. 
Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

                    BALANCED BINARY TREE
#* A balanced binary tree, also referred to as a height-balanced binary tree. 
It is a type of binary tree in which the difference between the height of the left and the right subtree for each node is either 0 or 1.

#? difference between the left and the right subtree for any node is not more than one
#? the left subtree is balanced
#? the right subtree is balanced


                    BINARY SEARCH TREE(BST)
#* Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
#? It is called a binary tree because each tree node has a maximum of two children.
#? It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.

Rule: 
#? 1- All nodes of left subtree are less than the root node
#? 2- All nodes of right subtree are more than the root node
#? 3- Both subtrees of each node are also BSTs i.e. they have the above two properties

                    AVL TREE
#* is a self-balancing binary search tree in which each node maintains extra information called a balance factor whose value is either -1, 0 or +1.
AVL tree got its name after its inventor Georgy Adelson-Velsky and Landis.

Balance Factor
#* Balance factor of a node in an AVL tree is the difference between the height of the left subtree and that of the right subtree of that node.
#? Balance Factor = (Height of Left Subtree - Height of Right Subtree) or (Height of Right Subtree - Height of Left Subtree)


#* https://www.programiz.com/dsa/binary-tree
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.choices = ["inorder", "preorder", "postorder"]
    
    def order(self, choice: str):
        if choice == self.choices[1]: print(f'{self.value}', end=' ')
        if self.left : self.left.order(choice)
        if choice == self.choices[0]: print(f'{self.value}', end=' ')
        if self.right : self.right.order(choice)
        if choice == self.choices[2]: print(f'{self.value}', end=' ')
    
    def is_full_tree(self):
        if self is None: return True
        
        if self.left is None and self.right is None: return True
        
        if self.left is not None and self.right is not None:
            return (self.left.is_full_tree() and self.right.is_full_tree())
        
        return False  
        
    def is_perfect(self, deep: int, level = 0):
        # check is empty
        if self is None: return True
        
        if self.left is None and self.right is None: 
            return deep == level + 1
        
        if self.left is None or self.right is None: return False
        
        return (self.left.is_perfect(deep, level + 1) and 
                self.right.is_perfect(deep, level + 1)) # if it is a perfect tree, return True        
    
    def is_balanced(self):
        if self is None: return True
        if abs(self.right.calculate_depth() - self.left.calculate_depth()) <= 1:
            return True
        return False
    
    def calculate_depth(self):
        deep = 0
        while self is not None:
            deep = deep + 1
            self = self.right or self.left
        return deep
    
    
    def insert_data(self, value):
        if self is None:
            return self.__class__(value) # create Node object
  
        if value < self.value:
            self.left = self.__class__(value) if self.left  is None else self.left.insert_data(value)
            """ if self.left is None:
                self.left = self.__class__(value)
            else:
                self.left = self.left.insert_data(value) """
            
        else:
            self.right = self.__class__(value) if self.right is None else self.right.insert_data(value)
            """ if self.right is None:
                self.right = self.__class__(value)
            else:
                self.right = self.right.insert_data(value) """
        return self

root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.left.left = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(7)

#root.order(choice="inorder")
#root.order(choice="preorder")
#root.order(choice="postorder")
#root.is_full_tree() # return true if the tree is full_tree
#root.is_perfect(root.calculate_depth())
#root.is_balanced()
#root.insert_data(13)
#print(_root.order(choice="inorder"))