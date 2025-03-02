class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def show_graph(self):
        for vertex in self.graph:
            print(f"{vertex}-->{self.graph[vertex]}")

graph = Graph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
print(graph.show_graph())