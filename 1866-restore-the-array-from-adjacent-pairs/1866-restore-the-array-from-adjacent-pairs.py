from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
        #find first instance where only 1 in list Size'
        currNode = -1
        for node, neighborList in graph.items():
            if len(neighborList) == 1:
                #u know its a edge
                currNode = node
                break
        ans = []
        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node, ans)
        dfs(currNode, None, ans)
        return ans

