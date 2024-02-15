from typing import Any

class Array:
    """! The DataStructure.Array class.
    
    Defines the basic array class.
    """
    
    def __init__(self, cap: int = 10, init_val = None) -> None:
        """! The array class initializer.
        
        @param cap The capacity of the array.
        
        @param init_val The value used to initialize the array. Default is None.
        """
        
        ## The capacity of the array
        self._cap = cap
        ## The array data, stored using a Pythong list
        self._data = [init_val for _ in range(self._cap)] 
        
    def __str__(self) -> str:
        """! A string representation of the array.
        
        @return A string that represents the array.
        """
        
        s = ''
        for elm in self._data:
            s += str(elm) + ", "
        return '[' + s.rstrip().rstrip(',') + ']'
        
    def __len__(self) -> int:
        """! The array length function.
        
        @return The length/capacity of the array.
        """
        
        return self._cap
        
    def _boundary_check(self, index: int) -> None:
        """! Check if an index is in bound, raise an error if not.
        
        @param index The input index.
        """
        
        if index < 0 or index >= self._cap:
            raise IndexError
        
    def __getitem__(self, index: int) -> Any:
        """! Get the item stored at index in the array.
        
        @param index The input index.
        
        @return The item stored at index.
        """
        
        self._boundary_check(index)
        return self._data[index]
        
    def __setitem__(self, index: int, value: Any):
        """! Store the input value at index in the array.
        
        @param index The input index.
        
        @param value The input value.
        """
        
        self._boundary_check(index)
        self._data[index] = value