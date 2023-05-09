class FoodStock:
    """
        A classe `FoodStock` representa um item de estoque de alimentos.
    """
    def __init__(self, name, manufacture_date, expiration_date):
        """
            O método `__init__` inicializa um novo objeto `FoodStock` com os valores dos parâmetros `name`, `manufacture_date` e `expiration_date`.
        """
        self.name = name
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date

    def __str__(self):
        """
            O método `__str__` retorna uma string formatada com as informações de fabricação e validade do objeto.
        """
        return f"fabricação = {self.manufacture_date}, validade = {self.expiration_date}"
