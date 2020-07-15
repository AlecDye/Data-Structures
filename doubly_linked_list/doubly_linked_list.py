"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    # helper methods
    # thanks after hours help
    def add_before(self, value):
        new_prev = self.prev
        self.prev = ListNode(self, value, new_prev)
        if new_prev:
            new_prev.next = self.prev

    def add_after(self, value):
        new_next = self.next
        self.next = ListNode(self, value, new_next)
        if new_next:
            new_next.next = self.next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if it is empty
        if self.head is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        else:
            # set head's prev to new_node
            # set new node's next to current head (self.head)
            # set head to the new node
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # use delete method
        # decrement length
        value = self.head.value
        self.delete(self.head)
        # self.length -= 1
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        # increment the DLL length attribute
        # if it is empty
        self.length += 1
        if self.tail is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        else:
            # set head's prev to new_node
            # set new node's next to current head (self.head)
            # set head to the new node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        # self.length -= 1
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # remove input node
        self.delete(node)
        # self.length -= 1
        # re-insert input node as head
        node.next = self.head
        self.head.next = node
        self.head = node
        self.length += 1

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # remove input node
        self.delete(node)
        # self.length -= 1
        # re-insert input node as tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # case: list empty
        if self.head is None:
            return None
        # case: single item in list
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        # case: 2 or more nodes
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
            self.length -= 1
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            self.length -= 1
        else:
            node.delete()
            # note: length should be adjusted after a check for empty list
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # case: list is empty
        if self.head is None:
            return None
        else:
            max_value = self.head.value
            current_node = self.head

            # use while loop?
            # so many node
            while current_node is not None:
                if current_node.value > max_value:
                    max_value = current_node.value

                current_node = current_node.next

            return max_value
