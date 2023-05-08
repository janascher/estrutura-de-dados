"""
    Importa a classe Node do arquivo node.py.
"""
from node import Node
from collections import deque


class AVLTree:
    """
        A classe `AVLTree` implementa uma árvore AVL, que é uma árvore binária de busca balanceada.
    """

    def __init__(self):
        """
            O método `__init__` é o construtor da classe, que inicializa a raiz da árvore.
        """
        self.root = None

    def insert(self, value):
        """
            O método `insert` insere um novo nó na árvore com o valor passado como parâmetro. Essa inserção é feita chamando o método `_insert` passando como parâmetro o valor e a raiz da árvore.
        """
        self.root = self._insert(value, self.root)

    def _insert(self, value, node):
        """
            O método privado `_insert` realiza a inserção de um novo nó na árvore.
        """
        if node == None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance_factor = self._get_balance_factor(node)

        if balance_factor > 1 and value < node.left.value:
            return self._rotate_right(node)

        if balance_factor < -1 and value > node.right.value:
            return self._rotate_left(node)

        if balance_factor > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance_factor < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_right(self, node):
        """
            O método privado `_rotate_right` realiza uma rotação à direita em um nó da árvore.
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        new_root.height = 1 + \
            max(self._get_height(new_root.left),
                self._get_height(new_root.right))

        return new_root

    def _rotate_left(self, node):
        """
            O método privado `_rotate_left` realiza uma rotação à esquerda em um nó da árvore.
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        new_root.height = 1 + \
            max(self._get_height(new_root.left),
                self._get_height(new_root.right))

        return new_root

    def _get_height(self, node):
        """
            O método privado `_get_height` recebe um nó e retorna a sua altura. Se o nó for nulo, a altura é 0.
        """
        if node == None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        """
            O método privado `_get_balance_factor` recebe um nó e retorna o fator de balanceamento, que é a diferença de altura entre as subárvores esquerda e direita.
        """
        if node == None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def print_tree(self):
        """
            O método `print_tree` imprime os nós da árvore em níveis.
        """
        if self.root == None:
            print("Árvore vazia")
            return

        queue = deque([(self.root, 0)])

        current_level = 0
        nodes_in_level = []
        while queue:
            node, level = queue.popleft()

            if level != current_level:
                print(" ".join(str(n.value) for n in nodes_in_level))
                nodes_in_level = []
                current_level = level

            nodes_in_level.append(node)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        print(" ".join(str(n.value) for n in nodes_in_level))


tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

print("Árvore balanceada:")
tree.print_tree()
