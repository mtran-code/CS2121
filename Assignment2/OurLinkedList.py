from Node import *


class OurLinkedList:
    """
    create a linked list class to contain a series of ordered nodes.
    """
    def __init__(self, head=None):
        """
        take first node in series of linked nodes as input.
        if no node input given, create empty linked list.
        establish the beginning (head) of the linked list.
        establish the end (tail) of the linked list.
        set the current node in the linked list.
        :param head: first node in series of linked nodes. (Node)
        """
        # if there is no input, create an empty linked list.
        if head is None:
            self.head = None
            self.tail = self.head

        else:
            self.head = head
            tail = head
            # cycle through list until last node is found, and set that node as the tail.
            while tail.next is not None:
                tail = tail.next
            self.tail = tail
        self.currNode = self.head

    def __str__(self):
        """
        create comma-separated string format of linked list for easier reference.
        :return: formatted list as string. (str)
        """
        # initialize empty string.
        listString = ""
        currNode = self.head

        # run through linked list and append all data values to string, separated by commas.
        while currNode is not None:
            listString += str(currNode.data) + ','
            currNode = currNode.next

        # remove trailing comma and enclose list string in square brackets.
        listString = listString.rstrip(',')
        return '[' + listString + ']'

    def __len__(self):
        """
        function to return length of linked list.
        :return: number of nodes in linked list. (int)
        """
        counter = 0
        currNode = self.head
        # run through linked list, adding one to counter for each node.
        while currNode is not None:
            counter += 1
            currNode = currNode.next

        return counter

    def __contains__(self, item):
        """
        determines if input item is a data value in any node in the linked list.
        :param item: data value to be searched for.
        :return: whether or not the item is found in the linked list. (bool)
        """
        exists = False
        currNode = self.head
        # run through linked list to see if value is found on each node.
        while currNode is not None:
            if currNode.data is item:
                exists = True
            currNode = currNode.next

        return exists

    def __eq__(self, other):
        """
        determines if the linked list is equivalent to another linked list based on data values and order.
        :param other: other linked list to compare current one to. (OurLinkedList)
        :return: whether or not the linked lists are equivalent. (bool)
        """
        equal = False
        if str(self) == str(other):
            equal = True

        return equal

    def __getitem__(self, index):
        """
        get an item in the linked list according to index number.
        :param index: specified index for node containing data value of interest. (int)
        :return: data value corresponding to node of input index.
        """
        # if the index is greater than the length of the list or if the index is negative, it is out of range.
        if index >= len(self) or index < 0:
            raise IndexError('list index is out of range')

        else:
            currNode = self.head
            for i in range(index):
                currNode = currNode.next

        return currNode.data

    def __setitem__(self, index, value):
        """
        edit a data value on a node within the linked list.
        :param index: specified index for node for which the data value should be altered. (int)
        :param value: data value to be changed to on the specified node.
        :return: None
        """
        # if the index is greater than the length of the list or if the index is negative, it is out of range.
        if index >= len(self) or index < 0:
            raise IndexError('list index is out of range')

        else:
            currNode = self.head
            for i in range(index):
                currNode = currNode.next
            currNode.data = value

    def __iter__(self):
        """
        initialize iterator beginning at head.
        :return: self
        """
        self.currNode = self.head
        return self

    def __next__(self):
        """
        iterate to the next node in the linked list, stopping when the final node is reached.
        :return: next node in the linked list. (Node)
        """
        # if there is no next node, stop the iteration.
        if self.currNode is None:
            raise StopIteration

        else:
            nextNode = self.currNode
            self.currNode = self.currNode.next
            return nextNode

    def getNode(self, index):
        """
        find a node in the linked list according to its index.
        :param index: index in the linked list to find the node. (int)
        :return: node at specified index. (Node)
        """
        # if the index is greater than the length of the list or if the index is negative, it is out of range.
        if index >= len(self) or index < 0:
            raise IndexError('list index is out of range')

        else:
            currNode = self.head
            for i in range(index):
                currNode = currNode.next
            return currNode

    def clear(self):
        """
        clear the entire linked list, making it empty.
        :return: None
        """
        self.head = None
        self.tail = None
        self.currNode = self.head

    def shallowCopy(self):
        """
        create a shallow copy of the linked list.
        :return: shallow copy of the linked list.
        """
        # return a variable referencing the same linked list as itself.
        copy = self
        return copy

    def deepCopy(self):
        """
        create a deep copy of the linked list.
        :return: deep copy of the linked list.
        """
        # if the list is empty (i.e. is None) then return None.
        if self.head is None:
            return None

        # create new nodes for every node in the linked list, and link them to each other.
        else:
            headCopy = Node(self.head.data)
            currentCopy = headCopy
            currNode = self.head.next
            while currNode is not None:
                currentCopy.next = Node(currNode.data)
                currentCopy = currentCopy.next
                currNode = currNode.next
            # create and return a new linked list made of newly created nodes.
            copy = OurLinkedList(headCopy)
            return copy

    def index(self, value):
        """
        find the index at which the first input value is found in the linked list.
        :param value: the data value to search for within the nodes of the linked list.
        :return: the index at which the input value's node is found in the linked list. (int)
        """
        counter = 0
        found = False
        # run through all nodes in linked list checking if data value matches.
        for node in self:
            # if the value is found, break the loop and return the counter
            if node.data is value:
                found = True
                break
            # if the value is not in the current node, add one to counter and check next node.
            else:
                counter += 1

        if found:
            return counter

        # if none of the nodes contain the value, raise value error.
        else:
            raise ValueError(str(value) + ' is not in the list')

    def append(self, value):
        """
        add a new node at the end of the linked list.
        :param value: data value associated with new node appended.
        :return: None
        """
        # if the linked list is empty, set both the head and tail as this newly made node.
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode

        # append the newly made node to the end of the linked list, and set it as the tail.
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, value):
        """
        add a new node at the beginning of the linked list.
        :param value: data value associated with the new node prepended.
        :return: None
        """
        # if the linked list is empty, set both the head and tail as this newly made node.
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode

        # append the newly made node to the beginning of the linked list, and set it as the head.
        else:
            newNode = Node(value, self.head)
            self.head = newNode

    def insert(self, index, value):
        """
        insert a new node at a specified index, replacing any existing nodes at the index and pushing them forward.
        :param index: the index to insert the new node. (int)
        :param value: the data value associated with the new node being inserted.
        :return: None
        """
        # if inserting at the beginning of the linked list, use prepend() function.
        if index is 0:
            self.prepend(value)

        # if inserting to the end of the list, use append() function.
        elif index is len(self):
            self.append(value)

        # insert node into linked list by changing previous and new node pointer.
        else:
            prevNode = self.getNode(index - 1)
            replacedNode = self.getNode(index)
            newNode = Node(value, replacedNode)
            prevNode.next = newNode

    def pop(self, index):
        """
        remove a node according to its index in the linked list.
        :param index: the index at which the node being removed is in the linked list. (int)
        :return: the data value of the node that was removed from the linked list.
        """
        # if list is empty, raise index error.
        if self.head is None:
            raise IndexError('pop from empty list')

        # if the index is greater than the length of the list or if the index is negative, it is out of range.
        elif index >= len(self) or index < 0:
            raise IndexError('pop index out of range')

        else:
            poppedNode = self.getNode(index)
            # if removing head of linked list, set the new head as next node.
            if index is 0:
                # if removing last node in linked list, set tail to None.
                if self.tail is poppedNode:
                    self.tail = None
                self.head = poppedNode.next

            # link the previous node to the node following the popped node.
            else:
                prevNode = self.getNode(index - 1)
                prevNode.next = poppedNode.next
                # if popping the last node, set the tail to the previous node.
                if self.tail is poppedNode:
                    self.tail = prevNode
            poppedNode.next = None

            return poppedNode.data

    def remove(self, value):
        """
        remove the first node from the linked list that contains the specified data value.
        :param value: data value for which the node being removed should contain.
        :return: the data value of the node that was removed from the linked list.
        """
        # take the index of the node containing input value and pop that node.
        removedIndex = self.index(value)
        self.pop(removedIndex)

    def reverse(self):
        """
        reverse the order of the linked list so that the head becomes the tail and vice versa.
        :return: None
        """
        currNode = self.head
        self.tail = self.head
        nextPlaceholder = None
        # beginning with first node, reverse all next node references to the previous node.
        for i in range(len(self)):
            tmp = currNode.next
            currNode.next = nextPlaceholder
            nextPlaceholder = currNode
            # set head to each node as it runs through the linked list, settling on the last node.
            self.head = currNode
            currNode = tmp
