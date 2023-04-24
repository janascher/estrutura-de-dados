class Node:
    """
        A classe `Node` representa um nó de uma lista duplamente encadeada.
    """
    def __init__(self, value):
        """
            O método `__init__` é o construtor da classe `Node` recebendo um parâmetro `value`, que é o valor armazenado no nó. Ele inicializa os atributos `value`, `next` e `previous` do nó:

                - Atributo `value`: armazena o valor contido no nó.

                - Atributo `next`: aponta para o próximo nó da lista encadeada.

                - Atributo `previous`: aponta para o nó anterior da lista encadeada.
        """
        self.value = value
        self.next = None
        self.previous = None
