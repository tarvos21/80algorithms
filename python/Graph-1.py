from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)    # A

    def addEdge(self, boy, girl):
        self.graph[boy].append(girl)    # B

    def BFS(self, start):
        visited = [False] * (len(self.graph))    # C
        queue = []
        queue.append(start)
        visited[start] = True    # D

        while queue:
            start = queue.pop(0)
            print(start, end=' | ')    # E

            for i in self.graph[start]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True    # F


graph = Graph()
graph.addEdge(0, 1)    # G
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)


print("广度优先搜索的结果是(从2开始)：")
graph.BFS(2)    # H
