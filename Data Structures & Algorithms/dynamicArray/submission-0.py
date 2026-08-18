class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity: 
            self.arr[i] = n


    def pushback(self, n: int) -> None:
        # insert n in the last position of the array

        if self.length == self.capacity: 
            self.resize()

        # insert at next empty position 
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # remove the last element in the array

        if self.length > 0: 
            self.length -= 1
            # soft delete the last element
        
        return self.arr[self.length]

    def resize(self) -> None:
        # creating new array with double capacity
        self.capacity = 2*self.capacity
        new_arr = [0] * self.capacity

        # copy elements into new arr
        for i in range(self.length): 
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity