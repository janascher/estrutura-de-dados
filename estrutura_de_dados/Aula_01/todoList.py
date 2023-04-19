"""
    A resolução apresentada é um exemplo de uso de uma estrutura de dados de array *não ordenado* é um sistema de gerenciamento de lista de tarefas. Nesse sistema, as tarefas são armazenadas em um array que não é ordenado, o que significa que elas não estão em uma ordem específica. Cada elemento do array representa uma tarefa e pode conter informações como o nome da tarefa, a data de criação e a data de vencimento.

    Ao adicionar uma nova tarefa, ela é simplesmente adicionada ao final do array. Para encontrar uma tarefa específica, é necessário percorrer todo o array em busca dela. Isso pode ser menos eficiente do que se a lista de tarefas fosse ordenada por data de vencimento, por exemplo, mas para listas pequenas ou que não precisam ser acessadas com frequência, o desempenho é aceitável.

    No entanto, se a lista de tarefas crescer muito, o desempenho pode ser afetado, especialmente se houver muitas operações de busca.
"""

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
