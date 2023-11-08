class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        distance = 0
        #take closest nut put to tree, while still nuts left, add left + right
        farthest = float('-inf')
        for nutY, nutX in nuts:
            distance += 2*(abs(nutY-tree[0]) + abs(nutX - tree[1]))
            farthest = max(farthest, abs(nutY - tree[0]) + abs(nutX - tree[1]) - abs(nutY - squirrel[0]) - abs(nutX - squirrel[1]))
        return distance - farthest