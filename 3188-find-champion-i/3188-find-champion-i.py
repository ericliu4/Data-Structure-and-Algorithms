class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for index, row in enumerate(grid):
            if sum(row) == n-1:
                return index