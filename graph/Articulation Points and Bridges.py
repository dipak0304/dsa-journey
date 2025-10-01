#Find articulation points and bridges in a graph.

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0  # Timer used in DFS

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph

    def _APB_util(self, u, visited, parent, low, disc, ap, bridges):
        children = 0
        visited[u] = True
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                self._APB_util(v, visited, parent, low, disc, ap, bridges)
                
                # Check if the subtree rooted at v has a connection back to ancestors of u
                low[u] = min(low[u], low[v])

                # Articulation point conditions
                if parent[u] is None and children > 1:
                    ap[u] = True
                if parent[u] is not None and low[v] >= disc[u]:
                    ap[u] = True

                # Bridge condition
                if low[v] > disc[u]:
                    bridges.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_articulation_points_and_bridges(self):
        visited = [False] * self.V
        disc = [float('inf')] * self.V
        low = [float('inf')] * self.V
        parent = [None] * self.V
        ap = [False] * self.V
        bridges = []

        for i in range(self.V):
            if not visited[i]:
                self._APB_util(i, visited, parent, low, disc, ap, bridges)

        articulation_points = [index for index, value in enumerate(ap) if value]
        return articulation_points, bridges


# Example usage
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

art_points, bridges = g.find_articulation_points_and_bridges()
print("Articulation Points:", art_points)
print("Bridges:", bridges)
