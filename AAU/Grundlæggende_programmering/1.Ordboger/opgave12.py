# opgave 12
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }


# opgave 12.a
g1 = {
    "a" : ["c"],
    "b" : ["c"],
    "c" : ["a", "b"]
}

g2 = {
    "a" : ["a", "b", "c", "d"],
    "b" : ["a", "b", "c", "d"],
    "c" : ["a", "b", "c", "d"],
    "d" : ["a", "b", "c", "d"]
}

g3 = {'a': ['f', 'c', 'd'],
      'b': ['g', 'e', 'd'],
      'c': ['h', 'a', 'e'],
      'd': ['i', 'b', 'a'],
      'e': ['j', 'b', 'c'],
      'f': ['a', 'g', 'j'],
      'g': ['b', 'h', 'f'], 
      'h': ['c', 'g', 'i'],
      'i': ['d', 'h', 'j'],
      'j': ['e', 'i', 'f']
}

class Graph(object):
    def __init__(self, graph_dict=None) -> None:
        if graph_dict is None:
            graph_dict = {}
        self._graph_dict = graph_dict
    # opgave 12.b
    def generate_edges(self) -> list:
        edges_list: list[tuple] = []
        for nodes in self._graph_dict:
            for edges in self._graph_dict[nodes]:
                if {nodes, edges} not in edges_list:
                    edges_list.append({nodes, edges})
        return edges_list
    # opgave 12.c
    def get_degree(self) -> dict:
        degree: dict[str, int] = {}
        for nodes, edges in self._graph_dict.items():
            degree[nodes] = len(self._graph_dict[nodes]) + int(nodes in edges)
        return degree
    # opgave 12.d
    def handshale_lemma(self) -> None:
        # sums degree values
        total_degree = sum(self.get_degree().values())
        # total edges times 2 
        total_edges = len(self.generate_edges()) << 1
        print(f"Total degree of nodes is {total_degree} 2 times nr. of edges is {total_edges}")

myGraph = Graph(g1)

degree = myGraph.handshale_lemma()

print(degree)
myGraph.handshale_lemma()