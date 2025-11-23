"""
test_selection.py
"""
import time
import random
from statistics import mean
from deterministic_selection import deterministic_select
from randomized_selection import randomized_select

def time_func(func, arr, k):
    start = time.perf_counter()
    res = func(arr, k)
    end = time.perf_counter()
    return res, end - start

def run_single_trial(n, distribution="random"):
    if distribution == "random":
        arr = [random.randint(0, 10*n) for _ in range(n)]
    elif distribution == "sorted":
        arr = list(range(n))
    elif distribution == "reversed":
        arr = list(range(n, 0, -1))
    elif distribution == "many_duplicates":
        arr = [random.randint(0, max(1, n//10)) for _ in range(n)]
    else:
        raise ValueError("unknown distribution")
    k = random.randrange(0, n)
    # run deterministic and randomized
    a_copy = list(arr)
    r1, t1 = time_func(deterministic_select, a_copy, k)
    r2, t2 = time_func(randomized_select, arr, k)
    # verify correctness
    expected = sorted(arr)[k]
    assert r1 == expected, f"deterministic mismatch: {r1} != {expected}"
    assert r2 == expected, f"randomized mismatch: {r2} != {expected}"
    return t1, t2

def bench(sizes=(1000, 5000, 10000), distributions=("random", "sorted", "reversed", "many_duplicates"), trials=5):
    print("Simple empirical benchmark (times in seconds)")
    print(f"{'n':>8} {'dist':>15} {'deterministic':>15} {'randomized':>15}")
    for n in sizes:
        for dist in distributions:
            t_det = []
            t_rand = []
            for _ in range(trials):
                td, tr = run_single_trial(n, dist)
                t_det.append(td)
                t_rand.append(tr)
            print(f"{n:8} {dist:15} {mean(t_det):15.6f} {mean(t_rand):15.6f}")

if __name__ == "__main__":
    # smaller sizes by default; increase for more thorough benchmarking
    bench(sizes=(100, 3000, 6000), trials=7)
