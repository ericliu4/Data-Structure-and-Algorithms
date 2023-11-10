class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for index1, num1 in enumerate(nums):
            for index2 in range(index1+indexDifference, n):
                if abs(nums[index2]-num1) >= valueDifference:
                    return [index1, index2]
        return [-1, -1]
