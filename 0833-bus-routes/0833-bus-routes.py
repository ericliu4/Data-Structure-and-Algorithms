from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stop_to_routes = defaultdict(set)  
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(route_idx)

        queue = deque([(source, 0)]) 
        visited_stops = set([source])  
        visited_routes = set()  

        while queue:
            curr_stop, num_buses = queue.popleft()
            for route_idx in stop_to_routes[curr_stop]:
                if route_idx in visited_routes:
                    continue
                
                for next_stop in routes[route_idx]:
                    if next_stop == target:
                        return num_buses + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, num_buses + 1))

                visited_routes.add(route_idx)

        return -1
                