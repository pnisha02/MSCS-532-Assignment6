"""
randomized_selection.py
"""
from typing import List
import random

def _partition_inplace(a: List[int], low: int, high: int, pivot_index: int) -> (int, int):
    """
    Partition a[low:high+1] around a[pivot_index].
    Returns (left_end, right_start) indices of the equal-to-pivot block.
    """
    pivot_value = a[pivot_index]
    # move pivot to end
    a[pivot_index], a[high] = a[high], a[pivot_index]
    store = low
    for i in range(low, high):
        if a[i] < pivot_value:
            a[store], a[i] = a[i], a[store]
            store += 1
    # move pivot(s) to store.. store+count-1
    a[store], a[high] = a[high], a[store]
    # now store is pivot final position, but there can be duplicates; we'll separate equal region
    # expand left and right to include equals
    left = store
    right = store
    n = high + 1
    # move leftwards equals
    i = left - 1
    while i >= low:
        if a[i] == pivot_value:
            left = i
        else:
            break
        i -= 1
    # move rightwards equals
    i = right + 1
    while i < n:
        if a[i] == pivot_value:
            right = i
        else:
            break
        i += 1
    return left, right

def _quickselect_inplace(a: List[int], low: int, high: int, k: int) -> int:
    """
    In-place quickselect on a[low:high+1].
    k is 0-based index relative to the whole array (i.e., target is the k-th smallest overall).
    """
    while True:
        if low == high:
            return a[low]
        pivot_index = random.randint(low, high)
        left, right = _partition_inplace(a, low, high, pivot_index)
        # left..right inclusive are equal to pivot
        if k < left:
            high = left - 1
        elif k > right:
            low = right + 1
        else:
            return a[k]

def randomized_select(arr: List[int], k: int) -> int:
    """
    Public API: returns k-th smallest element (0-based).
    Does not modify input arr (works on a copy).
    """
    if not 0 <= k < len(arr):
        raise IndexError("k out of range")
    a = list(arr)
    return _quickselect_inplace(a, 0, len(a)-1, k)

if __name__ == "__main__":
    # quick self-test
    import random
    for _ in range(5):
        a = [random.randint(0, 100) for _ in range(20)]
        for k in range(len(a)):
            r = randomized_select(a, k)
            assert r == sorted(a)[k]
    print("randomized_select quick self-test passed.")
