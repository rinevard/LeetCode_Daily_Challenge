# 2023/11/11 Daily challenge
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        # construct a graph that graph[from][to] = cost
        self.graph = {i: {} for i in range(n)}
        for edge in edges:
            self.addEdge(edge)
            
    def addEdge(self, edge: List[int]) -> None:
        # construct a graph that graph[from][to] = cost
        st, ed, cost = edge
        self.graph[st][ed] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = {node: float('inf') for node in self.graph}
        dist[node1] = 0
        to_visit = [(0, node1)]  # 优先队列，存储 (距离, 节点)
        visited = set()

        while to_visit:
            min_dist, current_node = heapq.heappop(to_visit)
            if current_node in visited:
                continue

            # 如果当前节点是目标节点，则返回距离
            if current_node == node2:
                return min_dist

            # 更新与当前节点相邻的节点的距离
            for adj_node, cost in self.graph[current_node].items():
                new_dist = min_dist + cost
                if new_dist < dist[adj_node]:
                    dist[adj_node] = new_dist
                    heapq.heappush(to_visit, (new_dist, adj_node))
            
            visited.add(current_node)

        return -1  # 如果无法到达 node2，则返回 -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)