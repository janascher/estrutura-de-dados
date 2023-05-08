from graph import Graph


class BreadthFirstSearchTree:
    """
        A classe `BreadthFirstSearchTree` representa uma busca em largura em um grafo.
    """
    def __init__(self, graph):
        """
            O método `__init__` inicializa a busca em largura com um grafo.
        """
        self.graph = graph
        self.visited = set()
        self.queue = []

    def add_start_vertex(self, vertex):
        """
            O método `add_start_vertex` adiciona um vértice como vértice de partida para a busca em largura.
        """
        self.queue.append(vertex)
        self.visited.add(vertex)

    def breadth_first_search(self):
        """
            O método `breadth_first_search`executa a busca em largura no grafo a partir do vértice de partida. Imprime na tela os vértices visitados na ordem em que foram visitados.
        """
        while self.queue:
            current_vertex = self.queue.pop(0)
            print(current_vertex, end=" ")

            for adjacent_vertex in self.graph.adjacent_vertices(current_vertex):
                if adjacent_vertex not in self.visited:
                    self.queue.append(adjacent_vertex)
                    self.visited.add(adjacent_vertex)

    def print_path(self):
        """
            O método `print_path` imprime o caminho percorrido pela busca em largura.
        """
        path = ""

        for vertex in self.visited:
            path += vertex + " -> "

        path = path[:-4]
        print("\n")
        print(path)


graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.add_edge("E", "F")

search_tree = BreadthFirstSearchTree(graph)
search_tree.add_start_vertex("A")
search_tree.breadth_first_search()
search_tree.print_path()
