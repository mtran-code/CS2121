class BinaryTreeNode:

    def __init__(self, data=None):
        """
        constructor to initialize a single node in a binary tree.
        :param data: data value to be contained in the node. (int)
        """
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        """
        string format for binary tree node.
        :return: string of the data value associated with node. (str)
        """
        return str(self.data)
