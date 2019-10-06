# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:33:46 2019

@author: z.chen7
"""

# Tree terminology
"""
root 
node
level
parent node
child node
leaves: the nodes at the end that don't have any children

height
the height of a node is the number of edges between it and the furthest leaf on the tree
A leaf has a height of zero but the parent of a leaf has a height of one
the height of a tree overall is the height of the root node

depth
the depth of a node is the number of edges to the root.

Height and depth should move inversely.
If a node is closer to a leaf then it's further from the node
"""


# Binary Tree Practice
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)
    
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, "")[:-1]
    
    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
        
    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
            
        
# Set up tree
tree = BinaryTree(1)
tree.root.value        
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
tree.search(4) 
tree.search(6)

# Test print_tree
tree.print_tree()



# Binary Sorted Tree
"""
BST is sorted so every value on the left of a particular node is smaller than
it and every value on the right of a particular node"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        
class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
    def insert_helper(self, current, new_val):
        if new_val < current.value:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
        else:
            if current.right:
                self.insert_help(current.right, new_val)
            else:
                current.right = Node(new_val)
    
    def search(self, find_val):
        return self.search_helper(self.root, find_val)
            
    def search_helper(self, current, find_val):
        if current:
            if find_val == current.value:
                return True
            elif find_val < current.value:
                return self.search_helper(current.left, find_val)
            else:
                return self.search_helper(current.right, find_val)
        else:
            return False

# Set up binary sorted tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
tree.search(4)
tree.search(6)



# Heaps
"""
A Heap is a special Tree-based data structure in which the tree is a complete
binary tree. Generally, Heaps can be of two types:
    
    1. Max-Heap: a parent must always have a greater value than its child so 
    the root ends up being the biggest element.

    2. Min-Head: a parent has lower value than its child so the root 
    is the minimum element.


Heaplify is the operation in which we reorder the tree based on the heap property.

Though heaps are represented as trees, they are actually often stored as arrays.


#############
## MaxHeap ##
#############
1. complete binary tree
2. every node <= its parent

MaxHeap is fast:
    1. insert in O(log n)
    2. get max in O(1)
    2. remove max in O(log n)

Easy to implement using an Array:
    i = 4
    parent(i) = i//2
    left(i) = i*2
    right(i) = i*2 + 1

MaxHeap Operations:
    1. Push (insert):
        * add value to the end of array
        * float it up to its propoer position
        
    2. Peek (get max):
        * return the value at heap[1]
    
    3. Pop (remove max):
        * move max to the end of array
        * delete it
        * bubble down the item at index to its proper position
        * return max

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def _floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._floatUp(parent)
            
    def _bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        
        if len(self.heap) > left and self.heap[index] < self.heap[left]:
            self._swap(index, left)
            self._bubbleDown(left)
            
        if len(self.head) > right and self.heap[index] < self.heap[right]:
            self._swap(index, right)
            self._bubbleDown(right)

"""