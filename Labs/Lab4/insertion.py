# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned.
        value = theSeq[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the right during the search.
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

        # Put the saved value into the open slot.
        theSeq[pos] = value


key_list = [80, 7, 24, 16, 43, 91, 35, 2, 19, 72]
print("Before:", key_list)

insertionSort(key_list)
print("After:", key_list)
