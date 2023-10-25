# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = deque()
        queue.append((root, None))
        while queue:
            n = len(queue)
            level = set()
            for _ in range(n):
                node, par = queue.popleft()
                if node.right in level and par:
                    if par.left == node:
                        par.left = None
                    else:
                        par.right = None
                    return root

                if node.right:
                    queue.append((node.right, node))
                if node.left:
                    queue.append((node.left, node))
                level.add(node)
        return root

        