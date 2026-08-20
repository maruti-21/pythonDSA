#  Graph consists of a set of vertices (or nodes) and a set of edges 

#  if a graph is complete or almost  complete we should use adjancy matrix 
#  if the number of edges are few then we should use adjacency list

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addvertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edges(self, vertex1, vertex2):
        # check both vertices exist
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # for undirected graph
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, "->", self.adjacency_list[vertex])


# 🔹 Create Graph
mygraph = Graph()

mygraph.addvertex('A')
mygraph.addvertex('B')
mygraph.addvertex('C')
mygraph.addvertex('D')
mygraph.addvertex('E')

# 🔹 Add edges
mygraph.add_edges('A', 'B')
mygraph.add_edges('A', 'C')
mygraph.add_edges('B', 'D')
mygraph.add_edges('C', 'E')

# 🔹 Print graph
mygraph.print_graph()