class Node:
    """
    create a Node class to hold each entry in linked list.
    """
    def __init__(self, data=None, next=None):
        """
        takes input data and next linked node to create Node object.
        if no input data given, initialize empty Node.
        :param data: the data value associated with the node.
        :param next: the pointer to the next node in the linked list. (Node)
        """
        self.data = data
        self.next = next

    def __str__(self):
        """
        return the string form of the data value of the node.
        :return: the data value of the node as a string. (str)
        """
        return str(self.data)

    def __eq__(self, other):
        """
        determines if this node is equivalent to another node based on data value.
        :param other: other node to compare self to. (Node)
        :return: equivalence of node and other input node. (bool)
        """
        # if both nodes are empty, they are equivalent
        if self is None and other is None:
            return True

        # if both nodes are not empty and contain the same data values, they are equivalent.
        elif self is not None and other is not None and self.data == other.data:
            return True

        # if previous conditions are not met, the nodes are not equivalent.
        else:
            return False

