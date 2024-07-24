from .vehicle import Vehicle

class Car(Vehicle):
    """
    Classe que representa um carro, herda de Vehicle.
    """

    def __init__(self, brand, model, year, daily_price, doors):
        """
        Inicializa um novo carro.

        :param brand: Marca do carro
        :param model: Modelo do carro
        :param year: Ano do carro
        :param daily_price: Preço diário do aluguel
        :param doors: Número de portas
        """
        super().__init__(brand, model, year, daily_price)
        self.doors = doors

    def display_info(self):
        """
        Exibe informações do carro.

        :return: String com as informações do carro
        """
        return f"{super().display_info()}, Número de portas: {self.doors}"
