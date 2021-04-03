from typing import Any


class Array:
    def __init__(self):
        self.max_size = 1
        self.values = [None for _ in range(self.max_size)]
        self.size = 0
        self.sorted = False

    def __len__(self):
        return self.size

    def sort(self):
        self.values.sort()
        self.sorted = True

    def insert(self, index: int, item: Any):
        if index < 0 or index > self.size:
            raise IndexError()
        if self.size == self.max_size:
            self.max_size = self.max_size * 2
            new_values = [None for _ in range(self.max_size)]
            for i, value in enumerate(self.values):
               new_values[i] = value
            self.values = new_values
            del new_values
        if index == self.size or self.is_empty():
            self.values[index] = item
        else:
            for i, value in enumerate(self.values):
                self.values[i+1] = value
            self.values[index] = item
        self.size += 1
        return self.values

    def is_empty(self):
        return self.size == 0

    def __contains__(self, item):
        for i in self.values:
            if i == item:
                return True
        return False

    def __setitem__(self, index, value): # real signature unknown
        if index < 0 or index > self.size:
            raise IndexError()
        self.insert(item=value, index=self.size)

    def __getitem__(self, index):
        if index < 0 or index > self.size:
            raise IndexError()
        return self.values[index]

    def index(self, item):
        for i, value in enumerate(self.values):
            if item == value:
                return i
        return -1

    def append(self, item):
        self[self.size] = item

    def show(self):
        return self.values[:self.size]

    def remove(self, index):
        if index < 0 or index > self.size:
            raise IndexError()
        if index < self.size - 1:
            for i in range(index, self.size-1):
                self.values[i] = self.values[i+1]
            self.values[self.size-1] = None
        self.size -= 1

    def clear(self):
        """ Remove all items from list. """
        for i, value in enumerate(self.values):
            if value is not None:
                self.values[i] = None

    def copy(self):
        """ Return a shallow copy of the list. """
        new_values = [i for i in self.values]
        return new_values

    def count(self, item): # real signature unknown
        """ Return number of occurrences of value. """
        count = 0
        for value in self.values:
            if value ==  item:
                count += 1
        return count

    def extend(self, *args, **kwargs): # real signature unknown
        """ Extend list by appending elements from the iterable. """
        pass


    def pop(self, index): # real signature unknown
        """
        Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverse *IN PLACE*. """
        pass


if __name__ == '__main__':
    a = list()
    lst = Array()
    lst.append(1)
    assert lst[0] == 1
    lst.append(3)
    assert lst[1] == 3
    lst.append(5)
    assert lst[2] == 5
    assert lst.show() == [1, 3, 5]
    lst.remove(1)
    assert lst.show() == [1, 5]
    lst.remove(1)
    assert lst.show() == [1]
    lst.remove(0)
    assert lst.show() == []
