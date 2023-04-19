import numpy as np


class Pilled:
    def __init__(self):
        self.items = np.array([], dtype=int)

    def is_empty(self):
        """
            O método `is_empty` verifica se a pilha está vazia.
        """
        return len(self.items) == 0

    def push(self, item):
        """
            O método `push` adiciona um item no topo da pilha.
        """
        self.items = np.append(self.items, item)

    def pop(self):
        """
            O método `pop` remove o item do topo da pilha.
        """
        if self.is_empty():
            return None
        item = self.items[-1]
        self.items = self.items[:-1]
        return item

    def top(self):
        """
            O método `top` retorna o item no topo da pilha sem removê-lo
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        """
            O método `size` retorna o tamanho da pilha.
        """
        return len(self.items)
