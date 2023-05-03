class Node:
    """
        A classe `Node` representa um nó de uma árvore binária e armazena um par chave-valor.
    """
    def __init__(self, key, value):
        """
            O método `__init__(self, key, value)` é o construtor da classe. Recebe como argumentos a chave (`key`) e o valor (`value`) a serem armazenados no nó. Inicializa também os atributos `left` e `right` com o valor `None`.

            Atributos:

                - `key`: chave a ser armazenada no nó.
                - `value`: valor a ser armazenado no nó.
                - `left`: referência ao filho esquerdo do nó.
                - `right`: referência ao filho direito do nó.
        """
        self.key = key
        self.value = value
        self.left = None
        self.right = None
