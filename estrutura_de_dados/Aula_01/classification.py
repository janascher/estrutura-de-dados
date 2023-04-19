# AULA 01 - ARRAYS NÃO ORDENADO E ORDENADO
#
# EXERCÍCIO:
# Descrever um exemplo o mais real que descobrir sobre o uso de Estrutura de Dados.
#
# RESOLUÇÃO 2 - ARRAY ORDENADO:
# Um exemplo de uso de uma estrutura de dados com array ordenado é um sistema de classificação de alunos por notas em uma escola.
#
# Nesse sistema, cada aluno tem uma nota associada a ele. Essas notas são armazenadas em um array ordenado em ordem crescente ou decrescente.
#
# Ao inserir uma nova nota de um aluno, o algoritmo de inserção realiza uma busca no array para encontrar a posição correta da nova nota. Em seguida, o algoritmo desloca as notas subsequentes para a direita para abrir espaço para a nova nota e insere a nota na posição correta.
#
# Esse sistema permite uma rápida busca por alunos com notas específicas. Por exemplo, para encontrar todos os alunos com notas maiores que uma nota X, basta fazer uma busca na estrutura de dados e retornar todos os elementos subsequentes à posição da nota X.

import numpy as np


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
