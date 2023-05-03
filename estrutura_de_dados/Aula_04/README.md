## 📝 Exercício da Aula 04

### Questão 01 - Descrever uma aplicação de Listas usadas para Filas e Pilhas.

Um exemplo de uso pode ser um sistema de gerenciamento de estoque utilizando listas encadeadas como filas ou pilhas.

Para implementar o método FIFO (First-In, First-Out)*, cada nó da lista encadeada pode representar um produto, contendo informações como nome, quantidade, preço e data da compra. Quando um novo produto chega ao estoque, ele é adicionado no final da fila. Quando um produto é vendido, o primeiro produto da fila é removido e a quantidade vendida é subtraída da quantidade restante. Essa abordagem garante que os produtos que chegaram primeiro ao estoque sejam vendidos primeiro, evitando a expiração de produtos e garantindo que os mais antigos sejam vendidos antes.

Para implementar o método LIFO (Last-In, First-Out)**, cada nó da lista encadeada também representa um produto com informações como nome, quantidade, preço e data da compra. Quando um novo produto chega ao estoque, ele é adicionado no topo da pilha. Quando um produto é vendido, o produto mais recente adicionado ao estoque é removido e a quantidade vendida é subtraída da quantidade restante. Essa abordagem pode ser útil em situações em que a expiração de produtos não é uma preocupação, como em estoques de produtos não perecíveis.

Ambas as abordagens são implementadas usando listas encadeadas, com a inserção de novos produtos no final da fila ou no topo da pilha e a remoção de produtos no início da fila ou no topo da pilha. A lista encadeada permite que os produtos sejam adicionados e removidos eficientemente sem a necessidade de realocar a memória, tornando essa estrutura de dados ideal para um sistema de gerenciamento de estoque.

*FIFO (First-In, First-Out) significa "Primeiro a Entrar, Primeiro a Sair" e envolve a venda dos itens mais antigos em estoque primeiro.

**LIFO (Last-In, First-Out) significa "Último a Entrar, Primeiro a Sair" e envolve a venda dos itens mais recentes em estoque primeiro.