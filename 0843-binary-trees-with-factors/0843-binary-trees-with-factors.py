from functools import cache
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        @cache
        def dp(val):
            count = 1
            for value in arr:
                if val % value == 0 and val // value in arr:
                    count += dp(value) * dp(val // value)
            return count % (10**9+7)
        
        return sum(dp(ele) for ele in arr) % (10**9+7)
