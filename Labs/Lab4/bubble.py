# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n):
        # Bubble the largest item to the end.
        for j in range(0, n - i - 1):
            if theSeq[j] > theSeq[j + 1]:  # swap the j and j+1 items.
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp


key_list = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
print("Before:", key_list)

bubbleSort(key_list)
print("After:", key_list)
