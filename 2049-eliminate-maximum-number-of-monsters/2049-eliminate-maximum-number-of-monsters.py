class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for distance, spd in zip(dist, speed):
            time.append(distance / spd) 
        for index, ele in enumerate(sorted(time)):
            if index >= ele: 
                return index  
        return len(dist)