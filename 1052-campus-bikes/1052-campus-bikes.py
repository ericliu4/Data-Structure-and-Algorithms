import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        m,n = len(workers), len(bikes)
        bikeIsTaken = [False]*n
        heap = []
        WorkerToBikeDistance = [[] for _ in range(m)]
        for workerIndex, (workerX, workerY) in enumerate(workers):
            for bikeIndex, (bikeX, bikeY) in enumerate(bikes):
                distance = abs(workerX-bikeX) + abs(workerY-bikeY)
                heapq.heappush(WorkerToBikeDistance[workerIndex], (distance, workerIndex, bikeIndex))
            heapq.heappush(heap, heapq.heappop(WorkerToBikeDistance[workerIndex]))
        ans = [0]*m
        while heap:
            _, worker, bike = heapq.heappop(heap)
            if not bikeIsTaken[bike]:
                ans[worker] = bike
                bikeIsTaken[bike] = True
            else:
                heapq.heappush(heap, heapq.heappop(WorkerToBikeDistance[worker]))
        return ans

