class Solution:
    def sortVowels(self, s: str) -> str:
        lst = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowelList = []
        for ch in s:
            if ch in lst:
                vowelList.append(ch)
        vowelList.sort()
        newS = []
        index = 0
        for ch in s:
            if ch in lst:
                newS.append(vowelList[index])
                index+=1
            else:
                newS.append(ch)
        return ''.join(newS)
