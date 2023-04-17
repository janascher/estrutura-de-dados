# AULA 01 - ARRAYS NÃO ORDENADO E ORDENADO
#
# EXERCÍCIO:
# Descrever um exemplo o mais real que descobrir sobre o uso de Estrutura de Dados.
#
# RESOLUÇÃO 1 - ARRAY NÃO ORDENADO:
# Um exemplo de uso de uma estrutura de dados de array não ordenado é um sistema de gerenciamento de lista de tarefas. Nesse sistema, as tarefas são armazenadas em um array que não é ordenado, o que significa que elas não estão em uma ordem específica. Cada elemento do array representa uma tarefa e pode conter informações como o nome da tarefa, a data de criação e a data de vencimento.
#
# Ao adicionar uma nova tarefa, ela é simplesmente adicionada ao final do array. Para encontrar uma tarefa específica, é necessário percorrer todo o array em busca dela. Isso pode ser menos eficiente do que se a lista de tarefas fosse ordenada por data de vencimento, por exemplo, mas para listas pequenas ou que não precisam ser acessadas com frequência, o desempenho é aceitável.
#
# No entanto, se a lista de tarefas crescer muito, o desempenho pode ser afetado, especialmente se houver muitas operações de busca.

from datetime import datetime
import numpy as np


class Task:
    """
        A classe `Task` representa uma tarefa a ser realizada e possui atributos como nome da tarefa, data de criação e data de vencimento.
    """

    def __init__(self, name, date_creation, date_expiration):
        self.name = name
        self.date_creation = np.datetime64(
            datetime.strptime(date_creation, '%Y-%m-%d'))
        self.date_expiration = np.datetime64(
            datetime.strptime(date_expiration, '%Y-%m-%d'))


class TodoList:
    """
        A classe `TodoList` representa uma lista de tarefas a serem realizadas e possui um atributo tarefas que é um array NumPy.
        A classe possui os métodos `adicionar_tarefa` e `exibir_tarefas`.
    """

    def __init__(self):
        self.tasks = np.array([], dtype=[(
            'name', 'U50'), ('date_creation', 'datetime64[D]'), ('date_expiration', 'datetime64[D]')])

    def add_task(self, task):
        """
            O método `add_task` adiciona uma nova tarefa à lista de tarefas.
        """
        self.tasks = np.append(self.tasks, np.array(
            [(task.name, task.date_creation, task.date_expiration)], dtype=self.tasks.dtype))

    def show_tasks(self):
        """
            O método `show_tasks` exibe todas as tarefas na lista, juntamente com suas informações, como nome, data de criação e data de vencimento.
        """
        if len(self.tasks) == 0:
            print('Nenhuma tarefa encontrada.')
        else:
            for task in self.tasks:
                print(f'Nome: {task["name"]}')
                print(f'Data de criação: {task["date_creation"]}')
                print(f'Data de vencimento: {task["date_expiration"]}')
                print('-------------------------------------------')


# Cria uma lista de tarefas e adicionar algumas tarefas
list = TodoList()
list.add_task(Task('Comprar pão', '2023-04-17', '2023-04-18'))
list.add_task(Task('Lavar o carro', '2023-04-17', '2023-04-22'))
list.add_task(Task('Pagar contas', '2023-04-16', '2023-04-20'))

# Exibe as tarefas
list.show_tasks()

# #################################################################################
#
# RESOLUÇÃO 2 - ARRAY ORDENADO:
# Um exemplo de uso de uma estrutura de dados com array ordenado é um sistema de classificação de alunos por notas em uma escola.
#
# Nesse sistema, cada aluno tem uma nota associada a ele. Essas notas são armazenadas em um array ordenado em ordem crescente ou decrescente.
#
# Ao inserir uma nova nota de um aluno, o algoritmo de inserção realiza uma busca no array para encontrar a posição correta da nova nota. Em seguida, o algoritmo desloca as notas subsequentes para a direita para abrir espaço para a nova nota e insere a nota na posição correta.
#
# Esse sistema permite uma rápida busca por alunos com notas específicas. Por exemplo, para encontrar todos os alunos com notas maiores que uma nota X, basta fazer uma busca na estrutura de dados e retornar todos os elementos subsequentes à posição da nota X.


class ClassificationStudents:
    """
        A classe `ClassificacaoAlunos` representa uma coleção de notas de alunos, armazenadas em um array numpy ordenado.
    """

    def __init__(self):
        self.notes = np.array([], dtype=np.float32)

    def insert_note(self, note):
        """
            O método `insert_note` recebe uma nota como parâmetro e insere a nota no array de notas em sua posição correta, mantendo o array ordenado.
        """
        index = np.searchsorted(self.notes, note)
        self.notes = np.insert(self.notes, index, note)

    def fetch_notes_greater_than(self, note):
        """
            O método `fetch_notes_greater_than` recebe uma nota como parâmetro e retorna um novo array com todas as notas maiores que a nota dada.
        """
        index = np.searchsorted(self.notes, note, side='right')
        return self.notes[index:]

    def fetch_notes_less_than(self, note):
        """
            O método `fetch_notes_less_than` recebe uma nota como parâmetro e retorna um novo array com todas as notas menores que a nota dada.
        """
        index = np.searchsorted(self.notes, note, side='left')
        return self.notes[:index]

    def fetch_notes_equal_to(self, note):
        """
            O método `fetch_notes_equal_to` recebe uma nota como parâmetro e retorna um novo array com todas as notas iguais à nota dada.
        """
        indexes = np.where(self.notes == note)
        return self.notes[indexes]

    def show_notes(self):
        """
            O método `show_notes` exibe as notas armazenadas no array como uma string separada por vírgulas.
        """
        notes_str = ', '.join(map(str, self.notes))
        print(notes_str)


#classification = ClassificationStudents()

# classification.insert_note(7.0)
# classification.insert_note(8.5)
# classification.insert_note(6.0)
# classification.insert_note(9.0)
# classification.insert_note(6.5)
# classification.insert_note(7.5)

#print("Notas dos alunos:")
# classification.show_notes()

#notes_bigger_than_7 = classification.fetch_notes_greater_than(7)
#print("Notas maiores que 7:", ', '.join(map(str, notes_bigger_than_7)))

#notes_less_than_7 = classification.fetch_notes_less_than(7)
#print("Notas menores que 7:", ', '.join(map(str, notes_less_than_7)))

#notes_iguais_a_7 = classification.fetch_notes_equal_to(7)
#print("Notas iguais a 7:", ', '.join(map(str, notes_iguais_a_7)))
