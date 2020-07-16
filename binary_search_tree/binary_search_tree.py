"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # case 1: value is less than self.value (left)
        if value < self.value:
            # if there is no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            # else?
            else:
                # Repeat the process on left subtree
                # call insert within insert
                # left references leftmost subtree
                self.left.insert(value)

        # case 2: value is greater or equal than self.value (right)
        elif value >= self.value:
            # test assumes to the greater or equal
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # case 1: if self.value is equal to the target
        if self.value == target:
            return True

        # case 2: if target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                # need "return" to escape closure
                return self.left.contains(target)

        # case 3: anything not caught
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about left subtree (max will always be right most node)
        # iterate through the nodes using a loop construct
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call fn to start loop?
        fn(self.value)
        # runs while there is a left node
        if self.left is not None:
            # recursion
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        # no else because we want to run every node and not exclude any

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
