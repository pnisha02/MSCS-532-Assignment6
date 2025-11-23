"""
array_matrix.py
"""

from typing import List, Any

class SimpleArray:
    def __init__(self, initial=None):
        self._data = list(initial) if initial is not None else []

    def get(self, i: int) -> Any:
        return self._data[i]

    def set(self, i: int, val: Any) -> None:
        self._data[i] = val

    def append(self, val: Any) -> None:
        self._data.append(val)

    def insert(self, i: int, val: Any) -> None:
        # O(n) shift
        self._data.insert(i, val)

    def delete(self, i: int) -> Any:
        # O(n) shift
        return self._data.pop(i)

    def size(self) -> int:
        return len(self._data)

    def to_list(self) -> List[Any]:
        return list(self._data)

class SimpleMatrix:
    """Simple 2D matrix backed by nested lists, row-major."""
    def __init__(self, rows:int, cols:int, fill=0):
        assert rows >= 0 and cols >= 0
        self.rows = rows
        self.cols = cols
        self._data = [[fill for _ in range(cols)] for _ in range(rows)]

    def get(self, r:int, c:int):
        return self._data[r][c]

    def set(self, r:int, c:int, val):
        self._data[r][c] = val

    def num_rows(self):
        return self.rows

    def num_cols(self):
        return self.cols

    def row(self, r:int):
        return list(self._data[r])

    def col(self, c:int):
        return [self._data[r][c] for r in range(self.rows)]
