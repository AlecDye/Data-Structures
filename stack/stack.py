import sys

sys.path.append("../singly_linked_list/")
from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.size

    # STACK add to tail & remove from tail
    def push(self, value):
        # return self.storage.append(value)
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # if self.storage:
        #     return self.storage.pop()
        # else:
        #     return None
        if self.storage.head:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            return None
