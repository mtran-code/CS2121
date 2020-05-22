# Implementation of the unbounded Priority Queue ADT using a Python list 
# with new items appended to the end.


class PriorityQueue:
    # Create an empty unbounded priority queue.
    def __init__(self):
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the queue.
    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue.
    def enqueue(self, item, priority):
        # Create a new instance of the storage class and append it to the list.
        entry = _PriorityQEntry(item, priority)
        self._qList.append(entry)

    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        # Find the entry with the highest priority.
        highest_index = 0
        for i in range(len(self._qList)):
            # See if the ith entry contains a higher priority (smaller integer).
            if self._qList[i].priority < self._qList[highest_index].priority:
                highest_index = i

        # Remove the entry with the highest priority and return the item.
        entry = self._qList.pop(highest_index)
        return entry.item


# Private storage class for associating queue items with their priority.
class _PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


PQ = PriorityQueue()

PQ.enqueue(1, 5)
PQ.enqueue(2, 4)
PQ.enqueue(3, 6)
PQ.enqueue(4, 0)
PQ.enqueue(5, 1)
PQ.enqueue(6, 0)
PQ.enqueue(7, 50)

print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
