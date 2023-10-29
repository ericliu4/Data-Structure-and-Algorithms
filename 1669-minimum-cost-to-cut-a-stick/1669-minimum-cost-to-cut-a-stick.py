class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dp(leftRange, rightRange):
            ans = float('inf')
            for cut in cuts:
                if leftRange < cut < rightRange:
                    ans = min(ans, rightRange-leftRange + dp(leftRange, cut) + dp(cut, rightRange))
            return ans if ans != float('inf') else 0
        
        return dp(0, n)