from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        counterA = Counter()
        counterB = Counter()
        ans = []
        for index in range(len(A)):
            counterA[A[index]] += 1
            counterB[B[index]] += 1
            curr = 0
            for key, counter in counterA.items():
                curr += min(counter, counterB[key])
            ans.append(curr)
        return ans
