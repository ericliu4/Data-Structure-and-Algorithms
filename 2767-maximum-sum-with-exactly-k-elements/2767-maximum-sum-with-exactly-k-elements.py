class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return sum(num for num in range(max(nums), max(nums)+k))