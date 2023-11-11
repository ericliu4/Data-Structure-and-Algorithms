class Solution: 
    def addMinimum(self, word: str) -> int:
        ans = 0
        lttr = "abc"
        index = 0
        for ch in word:
            while ch != lttr[index]:
                ans += 1
                index += 1
                index %= 3
            index+=1
            index %= 3
        if index == 1:
            ans += 2  
        elif index == 2:
            ans += 1  

        return ans