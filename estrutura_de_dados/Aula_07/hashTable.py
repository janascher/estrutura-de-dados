from foodStock import FoodStock


class HashTable:
    """
        A classe `HashTable` é uma tabela hash que armazena itens de estoque de alimentos.
    """

    def __init__(self, size):
        """
            O método `__init__` inicializa uma nova tabela hash com tamanho `size`. A tabela é representada como uma lista de listas vazias.

            PS: O símbolo "_" (underline) é uma convenção em Python para indicar uma variável que não será utilizada no código. Em outras palavras, é uma variável de espaço reservado.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        """
            O método `hash` calcula o índice de hash para a chave `key` usando a função `hash()` do Python e o tamanho da tabela.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
            O método `insert` insere um novo item na tabela hash com a chave `key` e o valor `value`. O método primeiro calcula o índice de hash para a chave e adiciona o par (chave, valor) à lista correspondente na tabela.
        """
        index = self.hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        """
            O método `search` busca um item na tabela hash com a chave `key` e retorna seu valor. Se o item não for encontrado, o método levanta uma exceção.
        """
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise None

    def __str__(self):
        """
            O método `__str__` retorna uma string formatada com a tabela hash e seus itens.
        """
        result = ""
        print(f"{'='*20} Estoque de Alimentos {'='*20}")
        for i in range(self.size):
            result += f"{i} -> "
            for k, v in self.table[i]:
                result += f"[{k}: {v}], "
            result += "\n"
        print(result)

    def print_item(self, key):
        """
            O método `print_item` busca um item na tabela hash com a chave `key` e retorna uma string formatada com suas informações de fabricação e validade. Se o item não for encontrado, a função retorna uma mensagem indicando que o item não foi encontrado.
        """
        result = self.get_item(key)
        if result == None:
            return f"O item {key} não foi encontrado no estoque."
        else:
            print(f"{'='*20} Resultado da Consulta {'='*20}")
            return f"{result.name}: fabricação = {result.manufacture_date}, validade = {result.expiration_date}"


# Cria tabela hash com tamanho 10
table = HashTable(10)

# Adiciona itens à tabela hash
table.insert("Arroz", FoodStock("Arroz", "2022-01-01", "2023-01-01"))
table.insert("Feijão", FoodStock("Feijão", "2022-01-01", "2023-01-01"))
table.insert("Macarrão", FoodStock("Macarrão", "2022-01-01", "2023-01-01"))

# Imprimi a tabela hash
table.__str__()
