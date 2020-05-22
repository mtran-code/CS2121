from BinarySearchTree import *

totalScore = 0

try:
    bst = BinarySearchTree()
    totalScore += 5
    print("bst constructor works.")
except:
    print("Exception in constructor!")

try:
    bst.insert(5)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(3)
    bst.insert(1)
    bst.insert(8)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    totalScore += 10
    print("insert works.")
except:
    print("Exception in insert!")

# print("Check inOrder")
if bst.inOrder() == ['1', '2', '3', '4', '5', '5', '6', '7', '8', '9']:
    totalScore += 5
    print("inOrder works.")
else:
    print("inOrder Error")

# print("Check levelOrder")
if bst.levelOrder() == ['5', '2', '5', '1', '4', '8', '3', '6', '9', '7']:
    totalScore += 5
    print("levelOrder works.")
else:
    print("levelOrder Error")

# print("Check preOrder")
if bst.preOrder() == ['5', '2', '1', '4', '3', '5', '8', '6', '7', '9']:
    totalScore += 5
    print("preOrder works.")
else:
    print("preOrder Error")

# print("Check postOrder")
if bst.postOrder() == ['1', '3', '4', '2', '7', '6', '9', '8', '5', '5']:
    totalScore += 5
    print("postOrder works.")
else:
    print("postOrder Error")

# print("Check recursiveCount")
if bst.recursiveCount(bst.root) == 10:
    totalScore += 5
    print("recursiveCount works.")
else:
    print("recursiveCount Error")

try:
    bst2 = BinarySearchTree(bst.root.left)
    totalScore += 5
    print("bst2 constructor works.")
except:
    print("Exception in constructor!")

# print("Check recursiveCount")
if bst2.recursiveCount(bst2.root) == 4:
    totalScore += 5
else:
    print("bst2 recursiveCount Error")

try:
    bst3 = BinarySearchTree(bst.root.right)
    totalScore += 5
    print("bst3 constructor works.")
except:
    print("Exception in constructor!")

# print("Check recursiveCount")
if bst3.recursiveCount(bst3.root) == 5:
    totalScore += 5
    print("bst3 recursiveCount works.")
else:
    print("bst3 recursiveCount Error")

# An empty tree has a depth of -1
# print("Check depth")
if bst.depth() == 4:
    totalScore += 5
    print("depth works.")
else:
    print("depth Error")

# print("Check validate")
if bst.validate():
    totalScore += 5
    print("validate works.")
else:
    print("validate Error, false negative")

# print("Check search and levelOrder")
tmp = bst.search(6)
tmp.data = 99
if bst.levelOrder() == ['5', '2', '5', '1', '4', '8', '3', '99', '9', '7']:
    totalScore += 5
    print("search/levelOrder works.")
else:
    print("search/levelOrder Error")

# print("Check validate")
if not bst.validate():
    totalScore += 5
    print("validate works.")
else:
    print("validate Error, false positive")

# Fix it here
tmp.data = 6
# print("Check levelOrder")
if bst.levelOrder() == ['5', '2', '5', '1', '4', '8', '3', '6', '9', '7']:
    totalScore += 5
    print("levelOrder works.")
else:
    print("levelOrder Error")

# print("Check validate")
if bst.validate():
    totalScore += 5
    print("validate works.")
else:
    print("validate Error, false negative")

# print("Check Min")
if bst.findMin().data == 1:
    totalScore += 5
    print("checkMin works.")
else:
    print("checkMin Error")

# print("Check Max")
if bst.findMax().data == 9:
    totalScore += 5
    print("checkMax works.")
else:
    print("checkMax Error")

print("Your mark is %d" % int(totalScore))
