class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        queue = collections.deque()
        seen = set()
        seen.add((0,0))
        queue.append((0,0,0))

        directions = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (1,2), (1,-2), (2,1), (2,-1))

        while queue:
            row, col, step = queue.popleft()
            for dx, dy in directions:
                newRow = row+dy
                newCol = col+dx
                if (newRow, newCol) == (x,y):
                    return step+1
                if (newRow, newCol) not in seen:
                    seen.add((newRow, newCol))
                    queue.append((newRow, newCol, step+1))
        