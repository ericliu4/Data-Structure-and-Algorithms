class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def dp(k, n):
            if n==0 or n==1 or k==1:
                return n
            low = 1
            high = n
            while low+1<high:
                mid = (low+high)//2
                breaks = dp(k-1, mid-1)
                doesNotBreak = dp(k, n-mid)
                if breaks < doesNotBreak:
                    low = mid
                elif breaks > doesNotBreak:
                    high = mid-1
                else:
                    low = high = mid
            return 1+min(max(dp(k-1, mid-1), dp(k, n-mid)) for mid in (low, high))
        return dp(k, n)
