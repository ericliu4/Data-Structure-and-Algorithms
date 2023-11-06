import heapq
class SeatManager:

    def __init__(self, n: int):

        self.heap = [num for num in range(1,n+1)]
        

    def reserve(self) -> int:
        if len(self.heap) >= 1: return heapq.heappop(self.heap)
        return -1

        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        