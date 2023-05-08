from foodStock import FoodStock


class HashTable:
    def __init__(self, size):
        self.size = size
        """
        O símbolo "_" (underline) é uma convenção em Python para indicar uma variável que não será utilizada no código. Em outras palavras, é uma variável de espaço reservado.
        """
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise None

    def __str__(self):
        result = ""
        print(f"{'='*20} Estoque de Alimentos {'='*20}")
        for i in range(self.size):
            result += f"{i} -> "
            for k, v in self.table[i]:
                result += f"[{k}: {v}], "
            result += "\n"
        print(result)

    def print_item(self, key):
        result = self.get_item(key)
        if result == None:
                return f"O item {key} não foi encontrado no estoque."
        else:
            print(f"{'='*20} Resultado da Consulta {'='*20}")
            return f"{result.name}: fabricação = {result.manufacture_date}, validade = {result.expiration_date}"


# Criar tabela hash com tamanho 10
table = HashTable(10)

# Adicionar itens à tabela hash
table.insert("Arroz", FoodStock("Arroz", "2022-01-01", "2023-01-01"))
table.insert("Feijão", FoodStock("Feijão", "2022-01-01", "2023-01-01"))
table.insert("Macarrão", FoodStock("Macarrão", "2022-01-01", "2023-01-01"))


# Imprimir a tabela hash
table.__str__()

