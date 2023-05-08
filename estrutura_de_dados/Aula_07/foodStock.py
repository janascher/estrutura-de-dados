class FoodStock:
    def __init__(self, name, manufacture_date, expiration_date):
        self.name = name
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date

    def __str__(self):
        return f"fabricação = {self.manufacture_date}, validade = {self.expiration_date}"
