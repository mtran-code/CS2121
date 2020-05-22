from BinaryTreeNode import *


class BinarySearchTree:

    def __init__(self, root=None):
        """
        constructor to initialize BinarySearchTree class with class variables root and count.
        :param root: first node at the root of the binary tree, optional. (BinaryTreeNode)
        """

        self.root = root                        # root is root
        self.count = self.recursiveCount(root)  # count is count of root's subtree

    def __str__(self):
        """
        generates a string format for the tree using inOrder traversal.
        :return: list of node data values in order. (str)
        """

        return str(self.inOrder())  # calls string of inOrder traversal

    def insert(self, data):
        """
        inserts a data value into the binary tree at an appropriate location.
        :param data: desired data value to be added to the tree. (int)
        :return: None
        """

        if self.root is None:                       # if there is no root, set the data point as the new root
            self.root = BinaryTreeNode(data)

        else:
            self.recursiveInsert(data, self.root)   # recursive function to insert
        self.count += 1                             # after adding, add one to node count

    def recursiveInsert(self, data, node):
        """
        uses recursion to find the appropriate node at which a data value should be added.
        :param data: desired data value to be added to the tree. (int)
        :param node: root node under which to add data value. (BinaryTreeNode)
        :return: None
        """

        if data < node.data:                            # if insert data is less than current node data:
            if node.left is None:                       # add the insert as the left child if it doesn't exist
                node.left = BinaryTreeNode(data)
            else:                                       # OR move to the left child and check again
                self.recursiveInsert(data, node.left)

        elif data >= node.data:                         # if insert data is greater/equal to current node data:
            if node.right is None:                      # add the insert as the right child if it doesn't exist
                node.right = BinaryTreeNode(data)
            else:                                       # OR move to the right child and check again
                self.recursiveInsert(data, node.right)

    def search(self, data):
        """
        searches tree for a specified data value.
        :param data: data value to be searched for within binary search tree. (int)
        :return: node at which data value was found. (BinaryTreeNode)
        """

        return self.binarySearch(data, self.root)   # call binarySearch (recursive function)

    def binarySearch(self, data, node):
        """
        recursively searches through tree to find specified data value.
        :param data: data value to be searched for within binary search tree. (int)
        :param node: root node under which to search for data value. (BinaryTreeNode)
        :return: node at which data value was found. (BinaryTreeNode)
        """

        if node is None:                                # if the node doesnt exist, return None
            return None

        elif node.data is data:                         # if the node matches, return it
            return node

        elif data < node.data:                          # if the desired node is less than the current node,
            return self.binarySearch(data, node.left)   # move to the left child and check again

        elif data >= node.data:                         # if the desired node is greater than the current node,
            return self.binarySearch(data, node.right)  # move to the right child and check again

    def count(self):
        """
        counts the number of nodes contained within the tree.
        :return: number of nodes contained within the tree. (int)
        """

        return self.recursiveCount(self.root)   # calls recursiveCount

    def recursiveCount(self, node):
        """
        recursively counts the number of nodes contained within the tree.
        :param node: root node under which to count nodes. (BinaryTreeNode)
        :return: number of nodes contained within the tree. (int)
        """

        if node is None:                                    # if there is no node, don't add to count
            return 0

        else:                                               # when node exist:
            count = 1                                       # add one to count for node

            if node.left is not None:                       # check if left child exists to count it and its children
                count += self.recursiveCount(node.left)
            if node.right is not None:                      # check if right child exists to count it and its children
                count += self.recursiveCount(node.right)

            return count

    def depth(self):
        """
        determines the depth of the tree.
        :return: depth of the tree. (int)
        """

        return self.recursiveDepth(self.root)   # call recursiveDepth

    def recursiveDepth(self, node):
        """
        recursively determines the depth of the tree.
        :param node: root node under which to count the number of levels. (BinaryTreeNode)
        :return: the depth of the tree. (int)
        """

        depth = -1                                               # by default, depth is -1 (no root exists)
        if node is not None:                                     # if the node does exist,

            if node.left is None and node.right is None:         # if leaf node, depth is 0
                depth = 0

            else:
                if self.recursiveDepth(node.left) \
                        >= self.recursiveDepth(node.right):      # if the left child's depth is more than the right,
                    depth = 1 + self.recursiveDepth(node.left)   # add the depth of the left child's subtree plus one

                elif self.recursiveDepth(node.left) \
                        < self.recursiveDepth(node.right):       # if the right child's depth is more than the left,
                    depth = 1 + self.recursiveDepth(node.right)  # add the depth of the right child's subtree plus one

        return depth

    def inOrder(self):
        """
        lists the node data values in the tree according to InOrder traversal.
        :return: list of strings containing node data values. (list)
        """

        dataStringList = []                                 # declare list to hold node data values
        self.recursiveInOrder(self.root, dataStringList)    # call recursiveInOrder on the list

        return dataStringList

    def recursiveInOrder(self, node, dataStringList):
        """
        recursively appends the node data values within tree to list using InOrder traversal.
        :param node: root node under which to add node data values. (BinaryTreeNode)
        :param dataStringList: list to append data values to. (list)
        :return: None
        """

        if node is None:                                            # if the node doesn't exist, ignore it and move on
            pass

        else:
            if node.left is not None:                               # if left child exists, add its subtree in InOrder
                self.recursiveInOrder(node.left, dataStringList)

            dataStringList.append(str(node.data))                   # next add the node itself

            if node.right is not None:                              # if right child exists, add its subtree in InOrder
                self.recursiveInOrder(node.right, dataStringList)

    def preOrder(self):
        """
        lists the node data values in the tree according to PreOrder traversal.
        :return: list of strings containing node data values in tree. (list)
        """

        dataStringList = []                                 # declare list to hold node data values
        self.recursivePreOrder(self.root, dataStringList)   # call recursivePreOrder on the list

        return dataStringList

    def recursivePreOrder(self, node, dataStringList):
        """
        recursively appends the node data values within tree to list using PreOrder traversal.
        :param node: root node under which to add node data values. (BinaryTreeNode)
        :param dataStringList: list to append data values to. (list)
        :return:
        """

        if node is None:                                            # if node doesn't exist, ignore it and move on
            pass

        else:
            dataStringList.append(str(node.data))                   # first add the node itself

            if node.left is not None:                               # if left child exists, add its subtree in PreOrder
                self.recursivePreOrder(node.left, dataStringList)

            if node.right is not None:                              # if right child exists, add its subtree in PreOrder
                self.recursivePreOrder(node.right, dataStringList)

    def postOrder(self):
        """
        lists the node data values in the tree according to PostOrder traversal.
        :return: list of strings containing node data value in tree. (list)
        """

        dataStringList = []                                 # declare list to hold node data values
        self.recursivePostOrder(self.root, dataStringList)  # call recursivePostOrder on the list

        return dataStringList

    def recursivePostOrder(self, node, dataStringList):
        """
        recursively appends the node data values within tree to list using PostOrder traversal.
        :param node: root node under which to add node data values. (BinaryTreeNode)
        :param dataStringList: list to append data values to. (list)
        :return:
        """

        if node is None:                                            # if the node doesn't exist, ignore it and move on
            pass

        else:
            if node.left is not None:                               # if left child exists, add its subtree in PostOrder
                self.recursivePostOrder(node.left, dataStringList)

            if node.right is not None:                              # if right child exists, add its subtree in PostOrder
                self.recursivePostOrder(node.right, dataStringList)

            dataStringList.append(str(node.data))                   # add the node itself last

    def levelOrder(self):
        """
        lists the node data values in tree in order of level from top to bottom, left to right.
        :return: list of strings containing node data value in tree. (list)
        """

        if self.root is None:                                        # if there is no root, return None
            return None

        else:
            dataStringList = [str(self.root.data)]                   # declare list of data values, starting with root
            prev = [self.root]                                       # declare list of nodes on previous level

            for level in range(self.depth()):                        # iterate through every level in the tree
                cur = []                                             # declare list of nodes on current level

                for node in prev:                                    # for every node on previous level:
                    if node.left is not None:                        # if it has a left child,
                        dataStringList.append(str(node.left.data))   # add the child to string list and
                        cur.append(node.left)                        # to list of nodes on current level

                    if node.right is not None:                       # if it has a right child,
                        dataStringList.append(str(node.right.data))  # add the child to the string list and
                        cur.append(node.right)                       # to list of nodes on current level

                prev = cur                                           # current list of nodes now becomes previous list

            return dataStringList                                    # return the string list after all levels are done

    def findMax(self):
        """
        find the greatest node data value within the tree.
        :return: node containing the maximum data value. (BinaryTreeNode)
        """

        return self.recursiveMax(self.root)     # call recursiveMax

    def recursiveMax(self, node):
        """
        recursively find the node containing the greatest data value in the tree.
        :param node: root node under which to search for max. (BinaryTreeNode)
        :return: node containing the maximum data value. (BinaryTreeNode)
        """

        if node.right is None:                      # if there is no right child, return the node
            return node

        else:                                       # if there is a right child, move to that node and check again
            return self.recursiveMax(node.right)

    def findMin(self):
        """
        find the lowest node data value within the tree.
        :return: node containing the minimum data value. (BinaryTreeNode)
        """

        return self.recursiveMin(self.root)     # call recursiveMin

    def recursiveMin(self, node):
        """
        recursively find the node containing the lowest data value in the tree.
        :param node: root node under which to search for min. (BinaryTreeNode)
        :return: node containing the minimum data value. (BinaryTreeNode)
        """

        if node.left is None:                       # if there is no left child, return the node
            return node

        else:                                       # if there is a left child, move to that node and check again
            return self.recursiveMin(node.left)

    def validate(self):
        """
        determine if the binary search tree is valid,
        i.e. left children are less than parent, right children are greater than parent.
        :return: validity of binary search tree. (bool)
        """

        valid = True                    # by default, set validity to True
        prev = 0                        # previously checked node value

        for data in self.inOrder():     # iterate through nodes using InOrder traversal
            if not int(data) >= prev:   # if the current node is less than the previous, tree is invalid
                valid = False
                break

            else:                       # if the node is greater than the previous, continue to next and keep checking
                prev = int(data)

        return valid


...
# Question 1 Response:
# EXAMPLE TREE:
#              (+)
#            /     \
#         (*)       (-)
#        /   \     /   \
#      (A)   (B) (C)   (D)
# InOrder traversal produces an infix expression.       Example form:   (A * B) + (C - D)
# PreOrder traversal produces a prefix expression.      Example form:   + * A B - C D
# PostOrder traversal produces a postfix expression.    Example form:   A B * C D - +

# Question 2 Response:
# search() worst case time complexity:  O(h) or O(n)
# insert() worst case time complexity:  O(h) or O(n)
# Explanation:      both search() and insert() have the same time complexity, because in both cases, the recursion takes
#                   place for each new level in the tree until the desired node is found for search/insert. The worst
#                   case time complexity is therefore proportional to the height of the tree: O(h).
#
#                   The maximum height of a binary tree would be n, thus the worst case time complexity is O(n) for a
#                   binary tree with maximum height.
#
#                   The minimum number of levels in a binary tree is given by floor(log2(n))+1, thus the worst case time
#                   complexity is O(floor(log2(n)+1) for a binary tree with a minimum height.
#
#                   If the height of the binary tree is unknown, a general worst case time complexity for these
#                   functions is O(n).
