# Implementation of the Stack ADT using a singly linked list.
class Stack:
    # Creates an empty stack.
    def __init__(self):
        self._top = None
        self._size = 0

    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return self._top is None

    # Returns the number of items in the stack.
    def __len__(self):
        return self._size

    # Returns the top item on the stack without removing it.
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    # Removes and returns the top item on the stack.
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    # Pushes an item onto the top of the stack.
    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1

    def printStack(self):
        tmp = self._top
        while tmp is not None:
            print(tmp.item),
            tmp = tmp.next
        print

    # The private storage class for creating stack nodes.


class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link


a = 8
b = 2
c = 3
d = 4
e = 12

x = 15
y = 20
z = 15


def interpret_line(line):
    line_list = line.split(' ')
    stack = Stack()
    for i in line_list:
        if i is 'A':
            stack.push(a)
        elif i is 'B':
            stack.push(b)
        elif i is 'C':
            stack.push(c)
        elif i is 'D':
            stack.push(d)
        elif i is 'E':
            stack.push(e)
        elif i is 'X':
            stack.push(x)
        elif i is 'Y':
            stack.push(y)
        elif i is 'Z':
            stack.push(z)
        elif i is '+':
            value2 = stack.pop()
            value1 = stack.pop()
            stack.push(value1 + value2)
        elif i is '-':
            value2 = stack.pop()
            value1 = stack.pop()
            stack.push(value1 - value2)
        elif i is '*':
            value2 = stack.pop()
            value1 = stack.pop()
            stack.push(value1 * value2)
        elif i is '/':
            value2 = stack.pop()
            value1 = stack.pop()
            stack.push(value1 / value2)
    return str(stack.pop())


def interpret_csv(filename):
    file = open(filename, 'r')
    for line in file:
        line = line.rstrip('\n')
        print(line + ' = ' + interpret_line(line))


interpret_csv('postfix.csv')
