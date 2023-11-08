from collections import deque
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx == fx and sy == fy and t == 1):
            return False
        xDiff = abs(fx - sx)
        yDiff = abs(fy - sy)
        if t < max(xDiff, yDiff):
            return False
        return True