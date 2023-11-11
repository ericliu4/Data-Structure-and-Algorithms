import collections
import heapq
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = collections.defaultdict(list)
        self.n = n
        for node1, node2, cost in edges:
            self.graph[node1].append([node2, cost])

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])
        

    def shortestPath(self, node1: int, node2: int) -> int:
        arr = [float('inf') for _ in range(self.n)]
        arr[node1] = 0

        heap = []
        heap.append([0, node1])
        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_distance <= arr[curr_node]:
                for neighbor, cost in self.graph[curr_node]:
                    distance = curr_distance + cost
                    if distance < arr[neighbor]:
                        arr[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))

        return arr[node2] if arr[node2] != float('inf') else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)