import numpy as np
import time
import matplotlib.pyplot as plt


class SortAnalysis:

    def bubbleSort(self, array):
        """
        sorts with bubble sort.
        :param array: input array to be sorted. (np.array)
        :return: None
        """
        n = len(array)
        for i in range(1, n):

            counter = 0
            for j in range(n - i):
                # if the current value is more than the compared value, swap them
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
                else:
                    counter += 1
            # if no values have been swapped, exit sort because it is already sorted.
            if counter == n - i:
                break

    def insertionSort(self, array):
        """
        sorts with insertion sort.
        :param array: input array to be sorted. (np.array)
        :return: None
        """
        for i in range(1, len(array)):
            value = array[i]
            # find the spot in array to insert current value, and insert it
            while i > 0 and value < array[i - 1]:
                array[i] = array[i - 1]
                i -= 1

            array[i] = value

    def _merge(self, array, array1, array2):
        """
        merges 2 input arrays together and outputs product to array.
        :param array: desired output product of array merging. (np.array)
        :param array1: first array to be added. (np.array)
        :param array2: second array to be added. (np.array)
        :return: None
        """
        pos1 = 0 # position in array1
        pos2 = 0 # position in array2

        for i in range(len(array)):

            # if array1 is done, add the rest of array2
            if pos1 == len(array1):
                array[i] = array2[pos2]
                pos2 += 1

            # if array2 is done, add the rest of array1
            elif pos2 == len(array2):
                array[i] = array1[pos1]
                pos1 += 1

            # if array1 value is less than array2 value, add the array1 value to the array
            elif array1[pos1] <= array2[pos2]:
                array[i] = array1[pos1]
                pos1 += 1

            # if array2 value is less than array1 value, add the array2 value to the array
            elif array2[pos2] < array1[pos1]:
                array[i] = array2[pos2]
                pos2 += 1

    def mergeSort(self, array):
        """
        sorts with merge sort.
        :param array: input array to be sorted. (np.array)
        :return: None
        """
        n = len(array)
        # if n<=1, array is already sorted
        if not n <= 1:
            # split the array into 2 arrays of equal/close to equal sizes
            array1, array2 = np.array_split(np.copy(array), 2)

            # call recursive function by sorting both halves and joining them in order
            self.mergeSort(array1)
            self.mergeSort(array2)
            self._merge(array, array1, array2)

    def mergeSort2(self, array):
        """
        if below specified threshold, sorts with insertion sort; otherwise sorts with merge sort.
        :param array: input array to be sorted. (np.array)
        :return: None
        """
        n = len(array)
        threshold = 300 # threshold at which mergeSort takes over insertionSort
        if n <= threshold:
            self.insertionSort(array)
        else:
            self.mergeSort(array)

    def bucketSort(self, array):
        """
        sorts using bucket sort.
        :param array: input array to be sorted. (np.array)
        :return: None
        """
        n = len(array)

        # create list of n empty lists (buckets)
        B = [[] for bucket in range(n)]

        # determine the bucket for each element of array to be added
        for element in array:
            index = int(n * element)
            B[index].append(element)

        index_counter = 0
        # sort each bucket, then add them all up together
        for bucket in B:
            self.insertionSort(bucket)
            for element in bucket:
                array[index_counter] = element
                index_counter += 1

    def fibonacciArray(self, n):
        """
        generates array of fibonacci numbers of size n starting from 5.
        :param n: desired length of fibonacci array, minimum 2. (int)
        :return: generated fibonacci array. (np.array)
        """
        if n < 2:
            raise ValueError("Array cannot have length smaller than 2.")
        else:
            # empty array of desired size to be filled
            fib_array = np.empty(n, dtype=int)
            prev_fibonacci = 3
            current_fibonacci = 5
            for i in range(n):
                # add the current fibonacci number to the array, and set the new current and prev numbers
                fib_array[i] = current_fibonacci
                current_fibonacci = current_fibonacci + prev_fibonacci
                prev_fibonacci = fib_array[i]
        return fib_array

    def runSort(self, sortName, sizes, seed, log=False):
        """
        randomly generates arrays of varying sizes, and records time taken to sort each array.
        :param sortName: call to desired sorting function. (function)
        :param sizes: array of desired array sizes to be generated and sorted. (np.array)
        :param seed: seed for random generator. (int)
        :param log: if True, outputs sorting progress to console in real time. (bool)
        :return: array of times taken to sort generated arrays using specified sorting algorithm. (np.array)
        """
        np.random.seed(seed) # seed the generator to make same random arrays to be tested
        times = np.empty(len(sizes)) # empty array to hold the run times of the sorting
        for i in range(len(sizes)):
            if log:
                if i == 0:
                    print("\r...", end="")
                elif times[i - 1] < 10000:
                    print("\rprevious array sorted in " + str(round(times[i - 1], 2)) + " microseconds. ", end="")
                elif 10000 < times[i - 1] < 120000000:
                    print("\rprevious array sorted in " + str(round(times[i - 1] / 1000000, 2)) + " seconds. ", end="")
                elif 120000000 < times[i - 1] < 7200000000:
                    print("\rprevious array sorted in " + str(round(times[i - 1] / 60000000, 2)) + " minutes. ", end="")
                else:
                    print("\rprevious array sorted in " + str(round(times[i - 1] / 3600000000, 2)) + " hours. ", end="")
                print(str(i) + " out of " + str(len(sizes)) + " runs; " +
                      "currently sorting array of size " + str(sizes[i]) + "...", end="")
            A = np.random.rand(sizes[i]) # generate random array to be sorted
            start = time.time_ns() # start timer
            sortName(A) # begin sorting
            elapsed = (time.time_ns() - start) / 1000 # end timer
            times[i] = elapsed # add elapsed time to times array

        return times

    def runAnalysis(self, sortList, n, filename, log=False):
        """
        runs analysis of sorting algorithm speed, saves output graph to file.
        :param sortList: list of function calls to desired sorting algorithms to be analyzed. (list)
        :param n: number of arrays of increasing size to be tested for each sorting algorithm. (int)
        :param filename: name of pdf file output containing analysis graph. (str)
        :param log: if True, outputs sorting progress to console in real time. (bool)
        :return: None
        """
        sizes = self.fibonacciArray(n) # set sizes of arrays to be sorted according to fibonacci numbers
        seed = np.random.randint(1) # set random integer seed
        sortNameList = list()
        plt.clf() # clear any previous plots
        for sortName in sortList:
            if log:
                print(sortName.__name__ + " analysis:")
            sortNameList.append(sortName.__name__) # record the name of the sorting algorithm being tested
            times = self.runSort(sortName, sizes, seed, log) # collect sorting times data
            plt.loglog(sizes, times) # plot the data according to array size and sorting time
            if log:
                if times[-1] < 10000:
                    print("\rDone! Longest run time: " + str(round(times[-1], 2)) + " microseconds.")
                elif 10000 < times[-1] < 120000000:
                    print("\rDone! Longest run time: " + str(round(times[-1] / 1000000, 2)) + " seconds.")
                elif 120000000 < times[-1] < 7200000000:
                    print("\rDone! Longest run time: " + str(round(times[-1] / 60000000, 2)) + " minutes.")
                else:
                    print("\rDone! Longest run time: " + str(round(times[-1] / 3600000000, 2)) + " hours.")
                print(times, "\n")
        if log:
            print("\nANALYSIS COMPLETE\n\n")
        # set graph parameters
        plt.legend(sortNameList)
        plt.xlabel("array size")
        plt.ylabel("runtime (microseconds)")
        plt.savefig(filename + ".pdf")


# Generate Graphs:
a = SortAnalysis()
a.runAnalysis([a.bubbleSort, a.insertionSort, a.mergeSort, a.bucketSort], 16, "comparison1", log=True)
a.runAnalysis([a.mergeSort, a.bucketSort], 24, "comparison2", log=True)
a.runAnalysis([a.mergeSort, a.mergeSort2, a.bucketSort], 20, "comparison3", log=True)

# Question 1 Response:
# mergeSort is abe to sort the input array by continuously splitting the input array into halves. This continues
# recursively until it is only made up of single elements, after which these halves are rejoined in order one by one
# until the final two halves join a single sorted array. This is called "divide-and-conquer" because this quite
# literally divides up the array into smaller constituents and sorts and joins those faster than if you were to sort one
# large array.

# Question 2 Response:
# in bucketSort, the designated bucket of each element is designated by the length of the input array multiplied by the
# element value (float value between 0 and 1). As a result, the lower values are placed in lower bucket indices and the
# higher values are placed in higher buckets. When the bucket values are all collected at the end, this ensures that the
# values in the lower buckets will always be lower than the values contained in the higher buckets, so no sorting needs
# to be done between buckets.

# Question 3 Response:
# according to the graph in comparison1.pdf, bubbleSort and insertionSort seem to have the same rate of increase with a
# greater slope than the other algorithms. In addition, insertionSort seems to have a slightly faster run time than
# bubbleSort. Similarly, mergeSort and bucketSort appear to have a similar slope that is lower than that of both
# bubbleSort and insertionSort, however bucketSort has a faster run time than mergeSort. Since the graph is in a loglog
# scale, the time complexities for bubbleSort and insertionSort are likely exponential (n^2) as their lines appear
# linear. The time complexities for mergeSort and bucketSort must be n, logn, nlogn, etc because their lines are not
# linear.

# Question 4 Response:
# bucketSort seems indiscriminately better than mergeSort. bucketSort is the best sorting algorithm because it takes
# advantage of the order of the buckets to speed up the sorting. By first separating the elements into respective
# buckets, the joining of these buckets becomes much faster because you just need to join them in order. For mergeSort,
# a similar approach is made where the input array is split into subgroups, however, when these are rejoined, they must
# be sorted once again, which is less efficient. Thus, sorting into buckets based on elements is more effective than
# just dividing arrays into halves.

# Question 5 Response:
# comparison3.pdf shows that the mergeSort2 produces a faster sort time than mergeSort when the value of n is below a
# designated threshold of approximately 80. It even seems to beat out bucketSort for fastest sorting time for smaller
# sized arrays. mergeSort2 may be better than bucketSort in general cases because one thing that bucketSort relies on is
# its values being floats between 0 and 1 in order to determine which bucket to place into. While the code can be
# altered to accommodate for this, there are still cases where it is less effective. For example, if the distribution of
# the values in the array is minimal, or if the array contains an extremely large outlier, the bucket separation becomes
# inefficient.
