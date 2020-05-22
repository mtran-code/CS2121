from SortAnalysis import *
from copy import copy
from os.path import exists

# Setup Sort Method Check
n = 100
A = np.random.rand(n)
sortedA = copy(A)
sortedA.sort()
totalScore = 0

a = SortAnalysis()

# Check Bubble Sort
B = copy(A)
a.bubbleSort(B)
print('Testing bubbleSort:')
if all(B == sortedA):
    totalScore += 5
else:
    print("**********bubbleSort wrong!")

# Check Insertion Sort
B = copy(A)
a.insertionSort(B)
print('Testing insertionSort:')
if all(B == sortedA):
    totalScore += 5
else:
    print("**********insertionSort wrong!")

# Check Merge Sort
B = copy(A)
a.mergeSort(B)
print('Testing mergeSort:')
if all(B == sortedA):
    totalScore += 10
else:
    print(B)
    print("**********mergeSort wrong!")

# Check Merge Sort 2
B = copy(A)
a.mergeSort2(B)
print('Testing mergeSort2:')
if all(B == sortedA):
    totalScore += 5
else:
    print("**********mergeSort2 wrong!")

# Check Bucket Sort
B = copy(A)
a.bucketSort(B)
print('Testing bucketSort:')
if all(B == sortedA):
    totalScore += 10
else:
    print("**********bucketSort wrong!")

# Check Merge
C1 = np.random.rand(n // 2)
C2 = np.random.rand(n // 2)
C1.sort()
C2.sort()
C = np.concatenate((C1, C2))
sortedC = copy(C)
sortedC.sort()
a._merge(C, C1, C2)
print('Testing _merge')
if all(C == sortedC):
    totalScore += 5
else:
    print("**********_merge wrong!")

# Check Fibonacci Array
D = np.array([5, 8, 13, 21, 34])
E = a.fibonacciArray(5)
print('Testing fibonacciArray')
if all(D == E):
    totalScore += 5
else:
    print("**********fibonacciArray wrong!")
try:
    a.fibonacciArray(1)
except ValueError:
    totalScore += 5
except:
    print()

# Check RunSort
F = np.array([1, 10, 100, 1000])
print('Testing runSort')
bT = a.runSort(a.bubbleSort, F, 0)
mT = a.runSort(a.mergeSort, F, 0)
if bT[-1] > mT[-1]:
    totalScore += 5
else:
    print("**********runSort bubble vs. merge times wrong!")

iT = a.runSort(a.insertionSort, F, 0)
bT = a.runSort(a.bucketSort, F, 0)
if iT[-1] > bT[-1]:
    totalScore += 5
else:
    print("**********runSort insertion vs. bucket times wrong!")

# Check Analysis
a.runAnalysis([a.bubbleSort, a.bucketSort], 10, 'test')
if exists('test.pdf'):
    totalScore += 10
else:
    print("**********runAnalysis wrong!")

print("Your mark is %d" % int(totalScore * 1.5))
