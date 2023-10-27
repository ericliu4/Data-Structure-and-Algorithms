class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        start, maxLen = 0,1

        for i in range(1,len(s)):
            left, right = i - 1, i + 1
            #odd cases
            while left>=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    start = left
                    maxLen = right - left + 1
                left -= 1
                right += 1
            
            left,right = i-1, i
            #even cases
            while left>=0 and right<len(s) and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    start = left
                    maxLen = right - left + 1
                left -= 1
                right += 1

        return s[start: start+maxLen]
