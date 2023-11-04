class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        count = 0
        for index in left:
            count = max(count, index)
        for index in right:
            count = max(count, n-index)

        return count