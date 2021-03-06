class Graph(object):

    def __init__(self, graph_dict=None, directed=None):
        """ initializes a graph object
           If no dictionary or None is given,
           an empty dictionary will be used
        """
        if not graph_dict:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.__directed = directed

    def is_directed(self):
        if self.__directed:
            return "I am directed"

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
           between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
           graph "graph". Edges are represented as sets
           with one (a loop back to the vertex) or two
           vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour[0], vertex} not in edges:
                    edges.append({vertex, neighbour[0]})
        return edges

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
           in graph """
        if not path:
            path = []
        graph_local = self.__graph_dict
        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return path
        if start_vertex[0] not in graph_local:
            return None
        if self.__directed:
            print("I am directed")
            for vertex in graph_local[start_vertex[0]]:
                if vertex[0] not in path and vertex[1]:
                    print("!!! path, ", path)
                    extended_path = self.find_path(vertex[0], end_vertex, path)
                    if extended_path:
                        return extended_path
            return None
        else:
            print("I am undirected")
            for vertex in graph_local[start_vertex[0]]:
                if vertex[0] not in path:
                    extended_path = self.find_path(vertex[0], end_vertex, path)
                    if extended_path:
                        return extended_path
            return None

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    g = {"a": [["d", 1]],
         "b": [["c", 1]],
         "c": [["b", 1], ["c", 1], ["d", 1], ["e", 0]],
         "d": [["a", 0], ["c", 0]],
         "e": [["c", 1]],
         "f": []
         }

    graph = Graph(g, directed=True)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("Add an edge:")
    graph.add_edge({"a", "z"})

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x", "y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
    print("Find path a -> b:")
    print(graph.find_path("e", "d"))
