# 2023/11/12 Daily challenge
# https://leetcode.com/problems/bus-routes/

from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """ 计算从起点到终点所需的最少公交车数量 """
        if source == target:
            return 0

        # 创建stop-bus键值对
        stop_with_buses = {}
        for bus in range(len(routes)):
            for stop in routes[bus]:
                if stop not in stop_with_buses:
                    stop_with_buses[stop] = []
                stop_with_buses[stop].append(bus)

        # 初始化变量
        visited_buses = [False] * len(routes)
        visited_stops = {source}
        q = deque()

        # 将包含起始站点的路线添加到队列中
        for bus, route in enumerate(routes):
            if source in route:
                q.append(bus)
                visited_buses[bus] = True

        bus_count = 0

        # BFS
        while q:
            bus_count += 1
            n = len(q)
            for _ in range(n):
                cur_bus = q.popleft()
                # 如果当前bus能到达目的地，返回bus_count即可
                if target in routes[cur_bus]:
                    return bus_count

                for stop in routes[cur_bus]:
                    # 找到相邻的bus
                    if stop in visited_stops:
                        continue
                    visited_stops.add(stop)
                    for adj_bus in stop_with_buses[stop]:
                        if visited_buses[adj_bus]:
                            continue
                        visited_buses[adj_bus] = True
                        q.append(adj_bus)

        return -1