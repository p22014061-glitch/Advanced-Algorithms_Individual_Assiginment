class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)


    def remove_edge(self, start, end):
        if start in self.graph and end in self.graph[start]:
            self.graph[start].remove(end)

    def list_outgoing(self, vertex):
        return list(self.graph.get(vertex, []))
