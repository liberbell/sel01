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
            curr = curr.nextval
        return "[" + "->".join(nodes) + "]"
    
    def prepend(self, dataval):
        """insert a new element at the begging of the list"""

        self.head = Node(dataval=dataval, nextval=self.head)

    def append(self, dataval):
        """insert a new element at the end of the list"""

        if not self.head:
            self.head = Node(dataval=dataval)
            return

        curr = self.head

        while curr.nextval:
            curr = curr.nextval
        
        curr.nextval = Node(dataval=dataval)

    def add_after(self, middle_dataval, dataval):
        """insert a new element after the node with middle_dataval"""

        if middle_dataval is None:
            print("Data to insert after not specified")
            return

        curr = self.head
        while curr and curr.dataval != middle_dataval:
            curr = curr.nextval

        new_node = Node(dataval=dataval)

        new_node.nextval = curr.nextval
        curr.nextval = new_node

    def find(self, data):
        """search for the first element with `dataval` matching
        `data`. return the element or `None` if not found."""

        curr = self.head
        while curr and curr.dataval != data:
            curr = curr.nextval

        return curr

    def remove(self, data):
        """remove the first occurrence of `data` in the list."""
        curr = self.head
        prev = None

        while curr and curr.dataval != data:
            prev = curr
            curr = curr.nextval

        if prev is None:
            self.head = curr.nextval

        elif curr:
            prev.nextval = curr.nextval
            curr.nextval = None

    def reverse(self):
        """reverse the list in-place."""

        curr = self.head
        prev_node = None
        next_node = None

        while curr:
            nextval = curr.nextval
            curr.nextval = prev_node

            prev_node = curr
            curr = nextval

        self.head = prev_node

    def reverse_recursive(self):
        """reverse the list in place using recursion"""

        def recursion(curr, prev):
            if not curr:
                return prev