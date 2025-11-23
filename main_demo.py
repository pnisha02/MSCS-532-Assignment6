"""
main_demo.py
"""
import random
from PART1.deterministic_selection import deterministic_select
from PART1.randomized_selection import randomized_select
from PART2.array_matrix import SimpleArray, SimpleMatrix
from PART2.stack_queue import ArrayStack, ArrayQueue
from PART2.linked_list import SinglyLinkedList
from PART2.rooted_tree import TreeNode, dfs_collect, bfs_collect

def demo_selection():
    arr = [random.randint(0, 100) for _ in range(15)]
    k = 5
    print("Array:", arr)
    print(f"{k}-th smallest (0-based) via deterministic:", deterministic_select(arr, k))
    print(f"{k}-th smallest (0-based) via randomized:", randomized_select(arr, k))
    print("Sorted (for check):", sorted(arr))

def demo_structures():
    print("\n-- SimpleArray demo")
    a = SimpleArray([2,3,4])
    a.insert(100, 99)
    print("SimpleArray contents:", a.to_list())

    print("\n-- Stack demo")
    s = ArrayStack()
    s.push(4); s.push(5); s.push(6)
    print("pop:", s.pop())

    print("\n-- Queue demo")
    q = ArrayQueue()
    q.enqueue("n"); q.enqueue("m")
    print("dequeue:", q.dequeue())

    print("\n-- LinkedList demo")
    ll = SinglyLinkedList([10,20,30])
    ll.insert_at(5, 12)
    print("Linked list traverse:", ll.traverse())

    print("\n-- Rooted tree demo")
    root = TreeNode("root")
    c1 = TreeNode("child1"); c2 = TreeNode("child2")
    root.add_child(c1); root.add_child(c2)
    c1.add_child(TreeNode("grandchild"))
    print("DFS order:", dfs_collect(root))
    print("BFS order:", bfs_collect(root))

if __name__ == "__main__":
    demo_selection()
    demo_structures()
