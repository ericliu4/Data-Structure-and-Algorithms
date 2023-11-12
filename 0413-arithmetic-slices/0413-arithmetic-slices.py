class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        curr = nums[1]-nums[0]
        prev = nums[1]
        currLength = 2
        count = 0
        for right, val in enumerate(nums[2:], start=2):
            if val - prev == curr:
                count += currLength-1
                currLength += 1
            else:
                currLength = 2
                curr = val - prev

            prev = val
        return count
            