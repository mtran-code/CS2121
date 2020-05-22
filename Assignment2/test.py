#!/usr/bin/env python3
import sys
from io import StringIO
from Node import *
from OurLinkedList import *


def CheckOutput(expected, presented):
    if expected == presented:
        print("The output is the same as expected!", expected, presented)
        return 1
    else:
        print("^^^^^ This is not the expected output! ^^^^^", expected, presented)
        return 0


def tests():
    totalScore = 0
    # Check Node
    aNode = Node()
    aNode.data = 0.1
    bNode = Node(data=1.1, next=Node(data=2.21))
    aNode.next = bNode

    # Testing Nodes
    totalScore += CheckOutput('0.1', str(aNode))
    totalScore += CheckOutput('1.1', str(bNode))
    totalScore += CheckOutput('2.21', str(bNode.next))
    totalScore += CheckOutput(None, bNode.next.next)

    # Check List
    aList = OurLinkedList(aNode)
    bList = OurLinkedList(bNode)
    cList = aList.shallowCopy()
    dList = aList.deepCopy()
    aList.head.next.next.data = 55

    # Check List
    totalScore += CheckOutput('[0.1,1.1,55]', str(aList))
    totalScore += CheckOutput('[1.1,55]', str(bList))
    totalScore += CheckOutput('[0.1,1.1,55]', str(cList))
    totalScore += CheckOutput('[0.1,1.1,2.21]', str(dList))

    # check equals
    if not (aList == bList):
        totalScore += 1
    if (aList == cList):
        totalScore += 1
    if not (aList == dList):
        totalScore += 1

    # getitem
    totalScore += CheckOutput('0.1', str(aList[0]))

    try:
        aList[3]
    except IndexError:
        totalScore += 1
    try:
        aList[-3]
    except IndexError:
        totalScore += 1

    # appending
    aList.append(77)
    totalScore += CheckOutput('[0.1,1.1,55,77]', str(aList))
    totalScore += CheckOutput('77', str(aList[3]))

    # prepend
    aList.prepend(45)
    totalScore += CheckOutput('[45,0.1,1.1,55,77]', str(aList))
    totalScore += CheckOutput('45', str(aList[0]))

    # insertAt
    aList.insert(0, 100)
    aList.insert(len(aList), 101)
    aList.insert(3, 102)
    totalScore += CheckOutput('[100,45,0.1,102,1.1,55,77,101]', str(aList)) * 2
    if len(aList) == 8:
        totalScore += 1

    # empty/almost empty lists
    bList = OurLinkedList()
    bList.append(4)
    totalScore += CheckOutput('[4]', str(bList))

    try:
        print(bList.pop(-1))
    except IndexError:
        totalScore += 1
    try:
        print(bList.pop(1))
    except IndexError:
        totalScore += 1

    totalScore += CheckOutput('4', str(bList.pop(0))) * 2
    totalScore += CheckOutput('[]', str(bList))
    totalScore += CheckOutput(None, bList.head)
    totalScore += CheckOutput(None, bList.tail)

    # Updating tail properly
    totalScore += CheckOutput('101', str(aList.pop(len(aList) - 1))) * 2
    totalScore += CheckOutput('[100,45,0.1,102,1.1,55,77]', str(aList))
    totalScore += CheckOutput(None, aList.tail.next)

    # remove
    aList.remove(100)
    aList.remove(77)
    totalScore += CheckOutput('[45,0.1,102,1.1,55]', str(aList))
    if len(aList) == 5:
        totalScore += 1

    try:
        aList.remove(800)
    except ValueError:
        totalScore += 1

    # reverse
    aList.reverse()
    totalScore += CheckOutput('[55,1.1,102,0.1,45]', str(aList)) * 2
    totalScore += CheckOutput('55', str(aList.head))
    totalScore += CheckOutput('45', str(aList.tail))
    return totalScore * 2


def main():
    return tests()


print("Your mark is", main())
