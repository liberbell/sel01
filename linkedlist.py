class Node:
    """A node is a singly-linked list"""

    def __init__(self, dataval=None, nextval=None):
        self.dataval = dataval
        self.nextval = nextval

    def __repr__(self):
        return repr(self.dataval)