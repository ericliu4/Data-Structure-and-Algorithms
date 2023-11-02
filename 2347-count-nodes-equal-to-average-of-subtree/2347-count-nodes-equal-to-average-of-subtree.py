# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(node):
            nonlocal count
            if not node:
                return 0, 0
            total = node.val
            currNum = 1
            leftTotal, leftCount = helper(node.left)
            rightTotal, rightCount = helper(node.right)
            total += leftTotal+rightTotal
            currNum += leftCount+rightCount
            if node.val == total//currNum:
                count += 1
            return total, currNum
        helper(root)
        return count