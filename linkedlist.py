class Node:
    """A node is a singly-linked list"""

    def __init__(self, dataval=None, nextval=None):
        self.dataval = dataval
        self.nextval = nextval

    def __repr__(self):
        return repr(self.dataval)

class LinkedList:
    def __init__(self):
        """creating a new singly-linked list."""

        self.head = None
    
    def __rper__(self):
        """creating a string represantation of the data in a list"""

        nodes = []
        curr = self.head

        while curr:
            nodes.append(repr(curr))