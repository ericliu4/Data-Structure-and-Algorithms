class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.Counter()
        for winner, loser in edges:
            graph[loser] += 1
            graph[winner] += 0
        champions = -1
        for i in range(n):
            if graph[i] == 0:
                if champions == -1:
                    champions = i
                else:
                    return -1
        return champions
        
