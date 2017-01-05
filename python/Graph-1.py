from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, boy, girl):
        self.graph[boy].append(girl)

    def BFS(self, start):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.pop(0)
            print(start, end = ' | ')

            for i in self.graph[start]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


print("广度优先搜索的结果是(从2开始)：")
g.BFS(2)
