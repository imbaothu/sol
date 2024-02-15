""" CSCI204 Stack lab
Last Modified by: Prof. Fuchsberger, March 2021
"""

from Array import Array

class MyStack:
    def __init__(self):
        self._size = 0
        self._capacity = 2  # Explicitly managing capacity
        self._array = Array(self._capacity,None)  # Initialize the Array with the specified capacity

    def is_empty(self):
        return self._size == 0

    def _expand(self):
        # Explicitly double the capacity
        self._capacity *= 2
        new_array = Array(self._capacity)  # Create a new Array with the updated capacity
        # Copy items from the old array to the new one
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array  # Update the stack's array to the new, larger array

    def push(self, item):
        if self._size >= self._capacity:  # Check if the current size reaches the capacity
            self._expand()
        self._array[self._size] = item
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        self._size -= 1
        item = self._array[self._size]
        self._array[self._size] = None  # Clear the slot where the item was removed
        return item

    def top(self):
        if self.is_empty():
            return None
        return self._array[self._size - 1]
    def __len__(self):
        return self._size
