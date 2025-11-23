"""
rooted_tree.py
"""

from typing import Any, List, Optional

class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.children: List['TreeNode'] = []

    def add_child(self, node: 'TreeNode'):
        self.children.append(node)

    def remove_child(self, node: 'TreeNode'):
        self.children.remove(node)

def dfs_collect(root: Optional[TreeNode]) -> List[Any]:
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.value)
        for c in reversed(node.children):
            stack.append(c)
    return res

def bfs_collect(root: Optional[TreeNode]) -> List[Any]:
    if root is None:
        return []
    res = []
    queue = [root]
    idx = 0
    while idx < len(queue):
        node = queue[idx]; idx += 1
        res.append(node.value)
        for c in node.children:
            queue.append(c)
    return res
