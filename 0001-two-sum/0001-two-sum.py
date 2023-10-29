from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        for index, val in enumerate(nums):
            if target - val in count:
                return [index, count[target-val]]
            count[val] = index  

