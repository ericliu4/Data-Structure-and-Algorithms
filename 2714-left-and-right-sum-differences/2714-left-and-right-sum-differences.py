class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = []
        for middle, val in enumerate(nums):
            right -= val
            ans.append(abs(right-left))
            left += val
        return ans