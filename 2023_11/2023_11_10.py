# 2023/11/10 Daily challenge
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # 由于不要求返回结果中数字的顺序，我们可以把结果视为一张无向图，两个节点间有边代表它们相邻。
        # 我们把每一个pair视为一个无向边，那么起点和终点就是只被一条边经过的节点。
        # 其它节点都被两条边经过。

        # 该函数在graph中加入一个无向边edge
        def graph_put(graph, edge):
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []    
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        # 预处理graph
        graph = {}
        for edge in adjacentPairs:
            graph_put(graph, edge)

        # 找到起点和终点（由于题目不要求顺序，起点和终点可以互换）
        st, ed = None, None
        for node in graph:
            if len(graph[node]) == 1 and st == None:
                st = node
            elif len(graph[node]) == 1 and ed == None:
                ed = node

        # 构建从起点到终点的路径
        visited = {node: False for node in graph}
        cur = st
        ans = []
        while cur != ed:
            visited[cur] = True
            ans.append(cur)
            cur = graph[cur][0] if not visited[graph[cur][0]] else graph[cur][1]

        # 在循环中我们没有把ed加入ans，最后我们把ed加入ans即可。
        ans.append(ed)
        return ans