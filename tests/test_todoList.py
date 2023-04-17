from io import StringIO
import sys
from estrutura_de_dados.Aula_01.todoList import Task, TodoList


def test_add_task():
    t1 = Task('Comprar pão', '2023-04-17', '2023-04-18')
    t2 = Task('Lavar o carro', '2023-04-17', '2023-04-19')
    tl = TodoList()
    tl.add_task(t1)
    tl.add_task(t2)
    assert len(tl.tasks) == 2
    assert tl.tasks[0]['name'] == 'Comprar pão'
    assert tl.tasks[1]['name'] == 'Lavar o carro'


def test_show_tasks():
    t1 = Task('Comprar pão', '2023-04-17', '2023-04-18')
    t2 = Task('Lavar o carro', '2023-04-17', '2023-04-19')
    tl = TodoList()
    tl.add_task(t1)
    tl.add_task(t2)

    # Redireciona a saída padrão para um objeto StringIO
    sys.stdout = StringIO()

    # Chama o método que escreve na saída padrão
    tl.show_tasks()

    # Obtém a saída do objeto StringIO e restaura a saída padrão
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__

    # Verifica se a saída corresponde ao esperado
    expected_output = 'Nome: Comprar pão\nData de criação: 2023-04-17\nData de vencimento: 2023-04-18\n-------------------------------------------\nNome: Lavar o carro\nData de criação: 2023-04-17\nData de vencimento: 2023-04-19\n-------------------------------------------\n'
    assert output == expected_output
