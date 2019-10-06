# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:34:22 2019

@author: z.chen7
"""

# Linked List 

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        """
        If the LinkedList already has a head, iterate through the next
        reference in every Element until you reach the end of the list.
        Set next for the end of the list to be the new_element. 
        Alternatively, if there is no head already, 
        you should just assign new_element to it and do nothing else.
        """
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
            
        else:
            self.head = new_element
          
    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.
        """
        counter = 1
        current = self.head
        
        if position < 1:
            return None
        
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        elif position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
            
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = None
        
        while current.value != value and current.next:
            prev = current
            current = current.next
        
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next


# Test Cases
# Set up some elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
    
# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
ll.head.next.next.value
ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
ll.get_position(3).value

# Test delete
ll.delete(1)
ll.head.value
ll.get_position(1).value
ll.get_position(2).value
ll.get_position(3).value





# Stack
"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        self.head = new_element
        
    def insert_first(self, new_element):
        """
        Insert new element as the head of the LinkedList"""
        new_element.next = self.head
        self.head = new_element
        
    def delete_first(self):
        """
        Delete the first (head) element in the LinkedList as return it"""
        deleted = self.head
        if deleted:
            self.head = deleted.next
            deleted.next = None
        return deleted
        

class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)
        
    def push(self, new_element):
        """
        Push (add) a new element onto the top of the stack"""
        self.ll.insert_first(new_element)
        
    def pop(self):
        """
        Pop (remove) the first element off the top of the stack and return it"""
        return self.ll.delete_first()
        
        
# Test case
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)
stack.ll.head.value
# Test Stack Functionality
stack.push(e2)
stack.push(e3)
stack.ll.head.value

stack.pop().value
stack.pop().value
stack.pop().value
stack.push(e4)
stack.pop().value





# Queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")    # Terry arrives
queue.append("Graham")    # Graham arrives
queue.popleft()   # The first to arrive now leaves
queue.popleft()   # The second to arrive now leaves
queue    # Remaining queue in order of arrival


"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue(object):
    def __init__(self, head=None):
        self.storage = [head]
        
    def enqueue(self, new_element):
        self.storage.append(new_element)
        
    def peek(self):
        return self.storage[0]
    
    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
q.peek()

# Test dequeue
q.dequeue()

# Test enqueue
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
q.peek()
q.storage


