class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA = 0
        countB = 0
        curr = None
        currCount = 0
        for color in colors:
            if color == 'A':
                if curr != 'A':
                    curr = 'A'
                    countB += max(currCount-2, 0)
                    currCount = 0
                currCount += 1
            else:
                if curr == 'A':
                    curr = 'B'
                    countA += max(currCount-2, 0)
                    currCount = 0
                currCount += 1
        if curr == 'A':
            countA += max(currCount-2, 0)
        else:
            countB += max(currCount-2, 0)
        return countA > countB
