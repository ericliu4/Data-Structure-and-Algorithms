class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        curr = max(nums)
        ans = curr
        for _ in range(k-1):
            curr += 1
            ans += curr
        return ans