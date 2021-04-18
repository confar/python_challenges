from dataclasses import dataclass
from typing import Optional


@dataclass
class SingleLinkedNode:
    value: int
    next: Optional['SingleLinkedNode'] = None


@dataclass
class DoubleLinkedNode:
    value: int
    next: Optional['DoubleLinkedNode'] = None
    prev: Optional['DoubleLinkedNode'] = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        return f'head {self.head} tail {self.tail}'

    def find(self, value: int):
        current = self.head
        index = 0
        while current.next:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1 if not current.value == value else index

    def index(self, index: int):
        if index < 0 or index > self.size-1:
            raise IndexError()
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def add(self, new_node, index):
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_elem = self.index(index-1)
            new_node.next = previous_elem.next
            previous_elem.next = new_node
        self.size += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            previous_elem = self.index(index-1)
            previous_elem.next = previous_elem.next.next
        self.size -= 1

    def display(self):
        current = self.head
        out = [current.value]
        while current.next:
            out.append(current.next.value)
            current = current.next
        return out


class DoubleLinkedList(SingleLinkedList):
    def add(self, new_node, index):
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        if not self.tail:
            self.tail = new_node
            self.head.next = self.tail
            self.size += 1
            return
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            previous_elem = self.index(index-1)
            new_node.next = previous_elem.next
            new_node.prev = previous_elem
            previous_elem.next = new_node
            new_node.next.prev = new_node
        self.size += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            previous_elem = self.index(index-1)
            previous_elem.next = previous_elem.next.next
            previous_elem.next.prev = previous_elem
        self.size -= 1


lst1 = SingleLinkedList()
lst1.head = SingleLinkedNode(1, next=SingleLinkedNode(2, next=SingleLinkedNode(3)))
lst1.tail = SingleLinkedNode(3)
lst1.size = 3
assert lst1.index(1) == SingleLinkedNode(2, next=SingleLinkedNode(3))
assert lst1.find(2)
assert lst1.find(1) == 0
assert lst1.find(4) == -1

another_lst = SingleLinkedList()
another_lst.add(SingleLinkedNode(1), index=0)
assert another_lst.display() == [1]
another_lst.add(SingleLinkedNode(2), index=1)
assert another_lst.display() == [1, 2]
another_lst.add(SingleLinkedNode(1), index=2)
assert another_lst.display() == [1, 2, 1]
another_lst.add(SingleLinkedNode(6), index=1)
assert another_lst.display() == [1, 6, 2, 1]
another_lst.remove(2)
assert another_lst.display() == [1, 6, 1]

lst2 = DoubleLinkedList()
lst2.add(DoubleLinkedNode(1), index=0)
assert lst2.display() == [1]
lst2.add(DoubleLinkedNode(2), index=1)
assert lst2.display() == [1, 2]
lst2.add(DoubleLinkedNode(3), index=1)
assert lst2.display() == [1, 3, 2]
assert lst2.find(3) == 1
assert lst2.find(1) == 0
assert lst2.find(2) == 2
lst2.remove(1)
assert lst2.display() == [1, 2]
