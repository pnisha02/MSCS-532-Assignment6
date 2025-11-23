"""
deterministic_selection.py
"""
from typing import List
import math
import copy

def _insertion_sort(a: List[int]) -> List[int]:
    a = a[:]  # local copy
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def _median_of_list(a: List[int]) -> int:
    if not a:
        raise ValueError("median of empty list")
    s = _insertion_sort(a)
    return s[len(s)//2]

def _partition(a: List[int], pivot: int) -> (list[int], list[int], list[int]):
    """Return (less, equal, greater) partitions relative to pivot."""
    less, equal, greater = [], [], []
    for x in a:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)
    return less, equal, greater

def _select_mom(a: List[int], k: int) -> int:
    """
    Internal recursive selection using Median of Medians.
    a: list (not empty)
    k: 0-based index
    """
    n = len(a)
    if n == 1:
        return a[0]
    # For small lists, just sort and return
    if n <= 10:
        s = _insertion_sort(a)
        return s[k]

    # Step 1: partition into groups of 5 and compute medians
    groups = [a[i:i+5] for i in range(0, n, 5)]
    medians = [ _median_of_list(g) for g in groups ]

    # Step 2: find pivot = median of medians (recursively)
    pivot = _select_mom(medians, len(medians)//2)

    # Step 3: partition around pivot
    less, equal, greater = _partition(a, pivot)

    if k < len(less):
        return _select_mom(less, k)
    elif k < len(less) + len(equal):
        # pivot is the answer
        return pivot
    else:
        # adjust k relative to greater
        return _select_mom(greater, k - len(less) - len(equal))

def deterministic_select(arr: List[int], k: int) -> int:
    """
    Public API
    arr: list of comparable items
    k: 0-based index into sorted(arr)
    Returns k-th smallest item.
    """
    if not 0 <= k < len(arr):
        raise IndexError("k out of range")
    # use a shallow copy to avoid user-visible modification
    return _select_mom(list(arr), int(k))

if __name__ == "__main__":
    # small self-test
    import random
    for _ in range(5):
        a = [random.randint(0, 50) for _ in range(15)]
        for k in range(len(a)):
            r1 = deterministic_select(a, k)
            r2 = sorted(a)[k]
            assert r1 == r2, f"Mismatch: {r1} vs {r2} for k={k}"
    print("deterministic_select quick self-test passed.")
