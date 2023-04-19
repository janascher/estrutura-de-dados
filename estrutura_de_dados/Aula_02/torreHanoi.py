"""
    O código apresentado é uma implementação da solução para o problema da Torre de Hanoi.

    A Torre de Hanoi é um jogo inventado pelo matemático francês Édouard Lucas (1842-1891), que consiste em mover uma pilha de discos de uma haste para outra haste, respeitando as seguintes regras:

        - Apenas um disco pode ser movido de cada vez;
        - Um disco maior não pode ser colocado sobre um disco menor;
        - Todos os discos devem ser movidos para a haste de destino, que não é a haste de origem.

    A configuração inicial do problema possui três hastes e um número `n` de discos empilhados em ordem crescente na haste de origem. O objetivo é mover todos os discos para a haste de destino, utilizando a haste auxiliar, seguindo as regras acima.
"""

from pilha import Pilled


class TowerOfHanoi:
    """
        A classe `TowerOfHanoi` possui três atributos:

            - `n`: número de discos que serão usados na torre;
            - `towers`: lista com 3 pilhas vazias, que representam as 3 torres. Inicialmente, a pilha de origem é preenchida com `n` discos;
            - `movements`: lista vazia que armazena os movimentos realizados para solucionar o problema.

        Além dos atributos, a classe possui os métodos `mover_disco`, `resolver` e `hanoi`.   
    """

    def __init__(self, n):
        """
            Este método é o construtor da classe e recebe como parâmetro o número de discos que serão usados na Torre de Hanoi. Ele inicializa os atributos `n`, `towers` e `movimentos`.

            Em seguida, é feito um loop que começa em `n` e decrementa 1 a cada iteração, preenchendo a pilha de origem (a primeira pilha da lista torres) com os discos em ordem decrescente.
        """
        self.n = n
        self.towers = [Pilled() for i in range(3)]
        self.movements = []

        for i in range(n, 0, -1):
            self.towers[0].push(i)

    def move_disk(self, origin, destiny):
        """
            Este método recebe como parâmetro a torre de origem e a torre de destino para movimentar um disco de uma torre para outra. Ele verifica se a torre de origem está vazia ou se a torre de destino já possui um disco e se esse disco é menor do que o disco que será movido. Se alguma dessas condições for verdadeira, o método retorna `None`. Caso contrário, o método remove o disco do topo da torre de origem e adiciona-o ao topo da torre de destino. Em seguida, é gerado uma string que descreve o movimento realizado e adicionada a lista de movimentos `self.movements`. O método retorna uma tupla contendo um valor booleano indicando se o movimento foi realizado com sucesso e a string que descreve o movimento.
        """
        if origin == destiny:
            return None
        if self.towers[origin].is_empty():
            return None
        if self.towers[destiny].is_empty() or self.towers[destiny].top() > self.towers[origin].top():
            disk = self.towers[origin].pop()
            self.towers[destiny].push(disk)

            movement = "Disco {} de {} para {}".format(
                disk, chr(ord("A") + origin), chr(ord("A") + destiny))
            self.movements.append(movement)

            return True, movement
        return movement

    def hanoi(self, n, origin, destiny, assistant):
        """
            Esse método é responsável por resolver o problema das Torres de Hanoi. Recebe 4 parâmetros:

                - `n`: número de discos que devem ser movidos da torre de origem para a torre de destino;
                - `origin`: o índice da torre de origem, representado por um número inteiro (0, 1 ou 2);
                - `destiny`: o índice da torre de destino, representado por um número inteiro (0, 1 ou 2);
                - `assistant`: o índice da torre auxiliar, representado por um número inteiro (0, 1 ou 2).

            Se `n` for igual a 1, o método chama o método `move_disk(self, origin, destiny)` para mover o disco da torre de origem para a torre de destino. Caso contrário, o método chama recursivamente o próprio método `hanoi`, com `n-1` discos, movendo-os da torre de origem para a torre auxiliar, em seguida move o disco restante da torre de origem para a torre de destino, e finalmente, chama recursivamente o próprio método `hanoi` novamente, com `n-1` discos, movendo-os da torre auxiliar para a torre de destino.
        """
        if n == 1:
            self.move_disk(origin, destiny)
        else:
            self.hanoi(n - 1, origin, assistant, destiny)
            self.move_disk(origin, destiny)
            self.hanoi(n - 1, assistant, destiny, origin)

    def solve(self):
        """
            Este método chama o método `hanoi` passando os parâmetros `self.n`, 0, 2 e 1. O método `hanoi` é responsável por resolver o problema da Torre de Hanoi.
        """
        self.hanoi(self.n, 0, 2, 1)

    def show_origin_tower(self):
        """
            Esse método não recebe parâmetros e não retorna nenhum valor. Ele imprime a mensagem informando qual é a torre de origem, utilizando o caractere 'A', e depois imprime o número de discos que ainda estão na torre de origem, utilizando o método `size()` da classe `Pilled`. 
        """
        print("\n")
        print(
            f"A torre de origem ({chr(ord('A') + 0)}) possui {self.towers[0].size()} discos.")
        print("\n")

    def show_result(self):
        """
            Esse método é responsável por imprimir os movimentos realizados para resolver o problema das Torres de Hanoi. Não recebe parâmetros e não retorna nenhum valor. O método itera sobre a lista de movimentos armazenados no atributo movimentos da classe `TowerOfHanoi` e imprime cada movimento. Cada movimento é uma string que informa qual disco foi movido e de qual torre para qual torre ele foi movido. O método imprime também uma mensagem informando o número de discos usados para a solução do problema.
        """
        print(f"Resultado para {self.n} discos:")
        for movimento in self.movements:
            print(movimento)
        print("\n")


n = 3  # Número de discos
torre = TowerOfHanoi(n)
torre.show_origin_tower()
torre.solve()
torre.show_result()
