class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        ans = float('inf')
        for middle, middleVal in enumerate(nums[1:-1], start = 1):
            left = right = float('inf')
            for leftVal in nums[:middle]:
                if leftVal < middleVal:
                    left = min(leftVal, left)
            for rightVal in nums[middle+1:]:
                if rightVal < middleVal:
                    right = min(rightVal, right)
            ans = min(ans, middleVal + left + right)
        return ans if ans != float('inf') else -1
