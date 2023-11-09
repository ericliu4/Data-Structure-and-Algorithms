class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        MOD = 10**9+7
        curr = None
        count = 0
        for ch in s:
            if ch == curr:
                count += 1
                total = (total + count)%MOD
            else:
                curr = ch
                count = 1
                total += count
        return total%MOD
        