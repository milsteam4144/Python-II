# CSC221
# M3HW
# 11/11/2018

"""
Author: Mallory Milstead
Create a class method, size() that uses the class variable _logicalSize
to return the logical size of an array (the number of indexes that contain
actual, relevant data)
"""


"""
File: arrays.py
An Array is like a list, but the client can use
only [], len, iter, and str.
To instantiate, use
<variable> = Array(<capacity>, <optional fill value>)
The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        
        self._logicalSize = 0
        """This will hold the logical size of the array"""

        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)
    
    def size(self):
        """->The logical size of the array(indexes that contain relevant data)"""
        #Reverse the array
        reverse = self._items[::-1]#Reverse the index to find "last" index that is not None
        for item in reverse: #Loop to check each item, starting at end index. 
            if item != None:
                #Logical size is the last instance of that item in the original list plus one
                self._logicalSize = (len(self._items) - self._items[::-1].index(item) - 1)  +1
                break# If it is not None, break loop
        return self._logicalSize

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]
        

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem
        
