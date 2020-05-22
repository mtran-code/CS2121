# Implementation of the Map ADT using closed hashing and a probe with double hashing.
from arrays import Array


# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    # Creates an empty map instance.
    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) // 3

        # Defines constants to represent the status of each table entry.
        self.UNUSED = None
        self.EMPTY = _MapEntry(None, None)

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the given key.
    def __contains__(self, key):
        slot = self._findSlot(key, False)
        return slot is not None

    # Adds a new entry to the map if the key does not exist.
    # Otherwise, the new value replaces the current value associated with the key.
    def add(self, key, value):
        if key in self:
            slot = self._findSlot(key, False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key, True)
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    # Returns the value associated with the key.
    def valueOf(self, key):
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key."
        return self._table[slot].value

    # Removes the entry associated with the key.
    def remove(self, key):
        slot = self._findSlot(key, False)
        self._table[slot] = self.EMPTY
        self._count -= 1

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return Array.__iter__(self._table)

    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion,
    # which locates the slot into which the new key can be added.
    def _findSlot(self, key, forInsert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)

        # Probe for the key.
        M = len(self._table)
        while self._table[slot] is not self.UNUSED:
            if not forInsert and (self._table[slot] is not self.EMPTY and self._table[slot].key == key):
                return slot
            elif forInsert and self._table[slot] is self.EMPTY:
                return slot
            else:
                slot = (slot + step) % M
        if forInsert:
            return slot

    # Rebuilds the hash table.
    def _rehash(self):
        # Create a new larger table.
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)

        # Modify the size attributes.
        self._count = 0
        self._maxCount = newSize - newSize // 3

        # Add the keys from the original array to the new table.
        key = 0
        for entry in origTable:
            if entry is not self.UNUSED and entry is not self.EMPTY:
                slot = self._findSlot(key, True)
                self._table[slot] = entry
                self._count += 1
            key += 1

    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        return abs(hash(key)) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)


# Quick function to visualize the contents of the hashmap.
def showHashMap(hashmap):
    array = []
    for i in range(len(hashmap._table)):
        if hashmap._table[i] is None:
            array.append("UNUSED")
        elif hashmap._table[i].value is None:
            array.append("EMPTY")
        else:
            array.append(hashmap._table[i].value)
    print(array)


# run testing commands
def test():
    # initialize empty hashmap
    h = HashMap()
    showHashMap(h)

    # add value 12 to key position 30
    h.add(30, 12)
    showHashMap(h)

    # replace previously added value 12 with value 16 at same key 30
    h.add(30, 16)
    showHashMap(h)

    # add value 12 to key position 337
    h.add(337, 12)
    showHashMap(h)

    # add value 17 to key position 37
    h.add(37, 17)
    showHashMap(h)

    # remove value from key position 30 (replaces UNUSED with EMPTY)
    h.remove(30)
    showHashMap(h)


test()
