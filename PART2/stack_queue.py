"""
stack_queue.py
"""

from typing import Any, List

class ArrayStack:
    """LIFO stack using list.append / list.pop (amortized O(1))."""
    def __init__(self):
        self._data: List[Any] = []

    def push(self, x: Any) -> None:
        self._data.append(x)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

class ArrayQueue:
    def __init__(self):
        self._data: List[Any] = []
        self._head = 0  # index of current front

    def enqueue(self, x: Any) -> None:
        self._data.append(x)

    def dequeue(self) -> Any:
        if self._head >= len(self._data):
            raise IndexError("dequeue from empty queue")
        val = self._data[self._head]
        self._head += 1
        if self._head > 64 and self._head > len(self._data) // 2:
            self._data = self._data[self._head:]
            self._head = 0
        return val

    def peek(self) -> Any:
        if self._head >= len(self._data):
            raise IndexError("peek from empty queue")
        return self._data[self._head]

    def is_empty(self) -> bool:
        return self._head >= len(self._data)

    def size(self) -> int:
        return len(self._data) - self._head
