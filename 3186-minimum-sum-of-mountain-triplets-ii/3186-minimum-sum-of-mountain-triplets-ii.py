class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        leftPrefix, rightPrefix = [], []
        for i, val in enumerate(nums):
            if i == 0 or val < leftPrefix[-1]:
                leftPrefix.append(val)
            else:
                leftPrefix.append(leftPrefix[-1])
        for index in range(n-1, -1, -1):
            if index == n-1 or nums[index] < rightPrefix[-1]:
                rightPrefix.append(nums[index])
            else:
                rightPrefix.append(rightPrefix[-1])
        for i in range(1, n-1):
            if leftPrefix[i-1]<nums[i] and rightPrefix[-1-i] < nums[i]:
                ans = min(ans, leftPrefix[i-1]+nums[i]+rightPrefix[-1-i])
        return ans if ans != float('inf') else -1