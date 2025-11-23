"""
linked_list.py
"""

from typing import Optional, Any, Iterable

class Node:
    def __init__(self, value: Any, nxt: 'Node'=None):
        self.value = value
        self.next = nxt

class SinglyLinkedList:
    def __init__(self, iterable: Optional[Iterable[Any]] = None):
        self.head: Optional[Node] = None
        self._size = 0
        if iterable:
            for val in iterable:
                self.append(val)

    def prepend(self, value: Any) -> None:
        self.head = Node(value, self.head)
        self._size += 1

    def append(self, value: Any) -> None:
        if not self.head:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(value)
        self._size += 1

    def insert_at(self, index: int, value: Any) -> None:
        if index <= 0:
            self.prepend(value)
            return
        if index >= self._size:
            self.append(value)
            return
        prev = None
        cur = self.head
        i = 0
        while i < index:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = Node(value, cur)
        self._size += 1

    def remove_at(self, index: int) -> Any:
        if self.head is None:
            raise IndexError("remove from empty list")
        if index <= 0:
            val = self.head.value
            self.head = self.head.next
            self._size -= 1
            return val
        prev = None
        cur = self.head
        i = 0
        while i < index and cur is not None:
            prev = cur
            cur = cur.next
            i += 1
        if cur is None:
            raise IndexError("index out of range")
        prev.next = cur.next
        self._size -= 1
        return cur.value

    def find(self, value: Any) -> int:
        cur = self.head
        i = 0
        while cur:
            if cur.value == value:
                return i
            cur = cur.next
            i += 1
        return -1

    def traverse(self) -> list:
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res

    def size(self) -> int:
        return self._size
