class Graph:
    """ 
        A classe `Graph" é uma implementação básica de um grafo.
    """

    def __init__(self):
        """
            O método `__init__` inicializa um grafo vazio, sem vértices e sem arestas.
        """
        self.vertices = {}

    def add_vertex(self, v):
        """
            O método `add_vertex` adiciona um vértice `v` ao grafo, se ele ainda não existir.
        """
        if v not in self.vertices:
            self.vertices[v] = []

    def add_edge(self, v1, v2):
        """
            O método `add_edge` adiciona uma aresta entre os vértices `v1` e `v2` ao grafo. Se os vértices ainda não existirem, eles são adicionados ao grafo. O grafo é não-direcionado, então a aresta é adicionada aos dois vértices.
        """
        if v1 in self.vertices:
            self.vertices[v1].append(v2)
        else:
            self.vertices[v1] = [v2]

        if v2 in self.vertices:
            self.vertices[v2].append(v1)
        else:
            self.vertices[v2] = [v1]

    def adjacent_vertices(self, v):
        """
            O método `adjacent_vertices` retorna uma lista com todos os vértices adjacentes (vizinhos) ao vértice `v` no grafo.
        """
        if v in self.vertices:
            return self.vertices[v]
        else:
            return []
