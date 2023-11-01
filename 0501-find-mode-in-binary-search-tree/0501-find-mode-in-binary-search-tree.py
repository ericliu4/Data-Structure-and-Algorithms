# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = collections.Counter()
        def dfs(node):
            if not node:
                return 
            counter[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        res = []
        dfs(root)
        modeCount = max(counter.values())
        for key, val in counter.items():
            if val == modeCount:
                res.append(key)
        return res