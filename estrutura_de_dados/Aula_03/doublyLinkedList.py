"""
    Importa a classe Node do arquivo node.py.
"""
from node import Node


class DoublyLinkedList:
    """
        A classe `DoublyLinkedList` representa uma lista duplamente encadeada, que armazena uma sequência de valores.
    """

    def __init__(self):
        """
            O método `__init__` inicializa a lista duplamente encadeada, criando duas referências `first_list` e `last_list`, ambas inicializadas como `None`.
        """
        self.first_list = None
        self.last_list = None

    def is_empty(self):
        """
            O método `is_empty` verifica se a lista está vazia. Retorna `True` se a lista estiver vazia ou `False`se for ao contrário.
        """
        return self.first_list == None

    def add_first(self, value):
        """
            O método `add_first` adiciona um novo valor no início da lista. Recebe um valor como parâmetro, cria um novo objeto `Node` com esse valor e insere no início da lista.
        """
        new_node = Node(value)

        if self.is_empty():
            self.first_list = new_node
            self.last_list = new_node

        new_node.next = self.first_list

        self.first_list.previous = new_node
        self.first_list = new_node

    def add_last(self, value):
        """
            O método `add_last` adiciona um novo valor no final da lista. Recebe um valor como parâmetro, cria um novo objeto `Node` com esse valor e insere no final da lista.
        """
        new_node = Node(value)

        if self.is_empty():
            self.first_list = new_node
            self.last_list = new_node

        new_node.previous = self.last_list

        self.last_list.next = new_node
        self.last_list = new_node

    def remove_first(self):
        """
            O método `remove_first` remove o primeiro elemento da lista. Se a lista está vazia, lança uma exceção. Caso contrário, retorna o valor removido.
        """
        if self.is_empty():
            raise Exception("Lista vazia.")

        value = self.first_list.value

        if self.first_list == self.last_list:
            self.first_list = None
            self.last_list = None
        else:
            self.first_list = self.first_list.next
            self.first_list.prev = None

        return value

    def remove_last(self):
        """
            O método `remove_last` remove o último elemento da lista. Se a lista está vazia, lança uma exceção. Caso contrário, retorna o valor removido.
        """
        if self.is_empty():
            raise Exception("Lista vazia.")

        value = self.last_list.value

        if self.first_list == self.last_list:
            self.first_list = None
            self.last_list = None
        else:
            self.last_list = self.last_list.previous
            self.last_list.next = None

        return value

    def remove_specified_value(self, value):
        """
            O método `remove_specified_value` remove o valor especificado da lista. Se a lista está vazia, lança uma exceção. Se o valor não é encontrado na lista, lança uma exceção. Caso contrário, remove o valor e retorna o objeto `Node` correspondente.
        """
        if self.is_empty():
            raise Exception("Lista vazia.")

        current = self.first_list

        while current.value != value:
            current = current.next

        if current == None:
            raise IndexError("Índice fora do intervalo.")

        if current == self.first_list:
            self.first_list = current.next
        else:
            current.previous.next = current.next

        if current == self.last_list:
            self.last_list = current.previous
        else:
            current.next.prev = current.previous

        return current

    def remove_at(self, index):
        """
            O método `remove_at` remove o valor na posição `index` da lista. Se a lista está vazia, lança uma exceção. Se a posição `index` é inválida, lança uma exceção. Caso contrário, remove o valor e retorna o valor removido.
        """
        if self.is_empty():
            raise Exception("Lista vazia.")

        current = self.first_list
        count = 1

        while current != None and count != index:
            current = current.next
            count += 1

        if current == None:
            raise IndexError("Índice fora do intervalo.")

        if current == self.first_list:
            self.first_list = current.next
        else:
            current.previous.next = current.next

        if current == self.last_list:
            self.last_list = current.previous
        else:
            current.next.previous = current.previous

        return current.value

    def show_list(self):
        """
            O método `show_list` exibe a lista. Se a lista está vazia, imprime "[]". Caso contrário, imprime uma lista de valores separados por vírgula e espaço, dentro de colchetes.
        """
        if self.is_empty():
            print("[]")
        else:
            current = self.first_list
            print("[", end=" ")

            while current != None:
                print(current.value, end=" ")

                if current.next != None:
                    print(", ", end=" ")
                current = current.next
            print("]")


# Cria uma lista duplamente encadeada vazia
list = DoublyLinkedList()

# Adiciona alguns elementos na lista e imprime a lista
list.add_first(1)
# list.add_first(3)
list.add_last(2)
# list.add_last(4)
list.show_list()

# Remove o primeiro elemento da lista e imprime a lista
# list.remove_first()
# list.show_list()

# Remove o último elemento da lista e imprime a lista
# list.remove_last()
# list.show_list()

# Remove um determinado valor especificado e imprime a lista
# list.remove_specified_value(2)
# list.show_list()

# Remove o elemento em uma posição e imprime a lista
# list.remove_at(1)
# list.show_list()

# print(list.first_list)
# print(list.last_list)
#print(list.first_list, list.last_list)
# print(list.first_list.previous)
# print(list.last_list.previous)
