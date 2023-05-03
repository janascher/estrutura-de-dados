"""
    Importa a classe Node do arquivo node.py.
"""
from node import Node


class BinaryTreeDict:
    """
        A classe `BinaryTreeDict` representa uma árvore binária que armazena um dicionário.
    """

    def __init__(self):
        """
            O método `init` é o construtor da classe. Inicializa o atributo `root` com o valor `None` e o atributo `dict` com um dicionário vazio.
        """
        self.root = None
        self.dict = {}

    def insert(self, key, value):
        """
            O método `insert` insere um novo par chave-valor na árvore. Recebe como argumentos a chave (`key`) e o valor (`value`). Se a árvore estiver vazia, cria um novo nó com a chave e o valor e o define como raiz. Caso contrário, percorre a árvore até encontrar um nó vazio e insere o novo nó como filho desse nó vazio. Armazena o par chave-valor no dicionário.
        """
        if self.root == None:
            self.root = Node(key, value)
            self.dict[key] = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left == None:
                        current_node.left = Node(key, value)
                        self.dict[key] = value
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right == None:
                        current_node.right = Node(key, value)
                        self.dict[key] = value
                        break
                    else:
                        current_node = current_node.right
                else:
                    self.dict[key] = value
                    break

    def get(self, key):
        """
            O método `get` retorna o valor associado a uma chave específica. Recebe como argumento a chave (`key`). Retorna `None` se a chave não existir no dicionário.
        """
        return self.dict.get(key)

    def remove(self, key):
        """
            O método `remove` remove um par chave-valor da árvore e do dicionário. Recebe como argumento a chave (`key`). Se a chave existir no dicionário, remove o par chave-valor do dicionário e chama o `método _remove_node` para remover o nó correspondente da árvore.
        """
        if key in self.dict:
            self.dict.pop(key)
            self.root = self.remove_node(self.root, key)

    def remove_node(self, node, key):
        """
            O método `_remove_node` remove um nó da árvore. Recebe como argumentos o nó (`node`) e a chave (`key`) do par chave-valor a ser removido. Retorna o nó modificado. Se o nó for nulo, retorna o próprio nó. Se a chave for menor que a chave do nó, chama recursivamente o método para o filho esquerdo do nó. Se a chave for maior que a chave do nó, chama recursivamente o método para o filho direito do nó. Caso contrário, verifica se o nó tem apenas um filho ou dois filhos. Se tiver apenas um filho, retorna esse filho. Se tiver dois filhos, encontra o menor nó do filho direito, substitui a chave e o valor do nó pelo menor nó e chama recursivamente o método para remover o menor nó da subárvore direita.
        """
        if node == None:
            return node
        elif key < node.key:
            node.left = self.remove_node(node.left, key)
            return node
        elif key > node.key:
            node.right = self.remove_node(node.right, key)
            return node
        else:
            if node.left == None:
                temp_node = node.right
                node = None
                return temp_node
            elif node.right == None:
                temp_node = node.left
                node = None
                return temp_node
            else:
                temp_node = self.get_min_value_node(node.right)
                node.key = temp_node.key
                node.value = temp_node.value
                node.right = self.remove_node(node.right, temp_node.key)
                return node

    def get_min_value_node(self, node):
        """
            O método `_get_min_value_node` retorna o menor nó de uma subárvore. Recebe como argumento o nó (`node`). Percorre a subárvore até encontrar o nó com o menor valor e o retorna.
        """
        current_node = node
        while current_node.left != None:
            current_node = current_node.left
        return current_node

    def preorder_traversal(self, node=None):
        """
            O método `preorder_traversal` percorre a árvore em pré-ordem e imprime as chaves e os valores dos nós. Recebe como argumento o nó (`node`) a partir do qual a árvore será percorrida. Se o nó não for especificado, a raiz da árvore é usada como ponto de partida.
        """
        if node == None:
            node = self.root
        if node != None:
            print(node.key, node.value)
            if node.left != None:
                self.preorder_traversal(node.left)
            if node.right != None:
                self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        """
            O método `inorder_traversal` percorre a árvore em ordem e imprime as chaves e os valores dos nós. Recebe como argumento o nó (`node`) a partir do qual a árvore será percorrida. Se o nó não for especificado, a raiz da árvore é usada como ponto de partida.
        """
        if node == None:
            node = self.root
        if node != None:
            if node.left != None:
                self.inorder_traversal(node.left)
            print(node.key, node.value)
            if node.right != None:
                self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        """
            O método `postorder_traversal` percorre a árvore em pós-ordem e imprime as chaves e os valores dos nós. Recebe como argumento o nó (`node`) a partir do qual a árvore será percorrida. Se o nó não for especificado, a raiz da árvore é usada como ponto de partida.
        """
        if node is None:
            node = self.root
        if node is not None:
            if node.left is not None:
                self.postorder_traversal(node.left)
            if node.right is not None:
                self.postorder_traversal(node.right)
            print(node.key, node.value)

    def print_connections(self):
        """
            O método `print_connections()` exibe o resultado das conexões dos nós da árvore.
        """
        print("Imprimindo as conexões:")
        node = self.root
        self.print_connections_recursive(node)

    def print_connections_recursive(self, node):
        """
            O método `print_connections_recursive` é um método auxiliar recursivo que imprime as conexões entre nós na árvore. Ele recebe um nó (`node`) como argumento e percorre a árvore recursivamente para imprimir todas as conexões entre os nós.
        """
        if node == None:
            return

        if node.left:
            print(str(node.key) + " --> " + str(node.left.key))
            self.print_connections_recursive(node.left)

        if node.right:
            print(str(node.key) + " --> " + str(node.right.key))
            self.print_connections_recursive(node.right)

    def print_get_result(self, key):
        """
            O método `print_get_result` imprime o resultado do método `get()` com a chave fornecida (`key`). Se a chave não for encontrada, imprime uma mensagem indicando que a chave não foi encontrada. Se a chave for encontrada, imprime o valor associado à chave.
        """
        result = self.get(key)
        if result is None:
            print(f"A chave {key} não foi encontrada.")
        else:
            print(f"O valor para a chave {key} é {result}.")

    def print_remove_result(self, key):
        """
            O método `print_remove_result` remove o nó com a chave fornecida (`key`) da árvore e imprime uma mensagem indicando que a chave está sendo removida. Em seguida, imprime as novas conexões na árvore após a remoção.
        """
        print("Removendo a chave", key)
        self.remove(key)
        print("Nova árvore")
        self.print_connections()

    def print_traversal(self, traversal_type):
        """
            O método `print_traversal` imprime os nós da árvore na ordem especificada (`traversal_type`). Se o tipo de passagem não for válido, imprime uma mensagem indicando que o tipo de passagem é inválido.
        """
        print(f"Imprimindo a árvore em {traversal_type}:")
        if traversal_type == "preorder":
            self.preorder_traversal()
        elif traversal_type == "inorder":
            self.inorder_traversal()
        elif traversal_type == "postorder":
            self.postorder_traversal()
        else:
            print(f"Tipo de ordem inválida: {traversal_type}")


tree = BinaryTreeDict()
tree.insert(4, "d")
tree.insert(2, "b")
tree.insert(6, "f")
tree.insert(1, "a")
tree.insert(3, "c")
tree.insert(5, "e")
tree.insert(7, "g")

tree.print_connections()

tree.print_get_result(5)

tree.print_remove_result(2)

tree.print_traversal("preorder")
tree.print_traversal("inorder")
tree.print_traversal("postorder")
