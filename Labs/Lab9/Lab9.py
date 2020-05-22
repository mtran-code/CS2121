from bubble import *
from insertion import *
from selection import *
from quicksort import *

import numpy as np
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(1500)


def generateArray(size, seed=np.random.randint(1)):
    np.random.seed(seed)
    array = np.random.rand(size)
    return array


def sortTime(array, sortName):
    start = time.time_ns()
    sortName(array)
    elapsed = time.time_ns() - start
    return elapsed/1000000


def sortAnalysis(arraySize, numRepetitions, sortList):
    results = []
    seeds = [np.random.randint(1) for repetition in range(numRepetitions)]
    arrays = [generateArray(arraySize, seeds[repetition]) for repetition in range(numRepetitions)]
    for sort in range(len(sortList)):
        reps = []
        times = []
        for repetition in range(numRepetitions):
            repetition_time = sortTime(arrays[repetition], sortList[sort])
            reps.append(repetition)
            times.append(repetition_time)
        plt.plot(reps, times)
        results.append(times)
    plt.legend([sortName.__name__ for sortName in sortList], loc="upper right")
    plt.xlabel("repetition number")
    plt.xticks(np.arange(numRepetitions), [i for i in range(1, numRepetitions + 1)])
    plt.ylabel("runtime (milliseconds)")
    plt.title("Sorting Algorithm time for "
              + str(numRepetitions)
              + " repetitions of array size "
              + str(arraySize) + ".")
    plt.savefig("output.pdf")
    output = ""
    for i in range(len(sortList)):
        output += sortList[i].__name__ + " times: " + str(results[i]) + "\n"
    return output


algorithms = [bubbleSort, selectionSort, insertionSort, quickSort]
analysis = sortAnalysis(1000, 10, algorithms)
print(analysis)
