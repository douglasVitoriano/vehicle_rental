from .vehicle import Vehicle

class Truck(Vehicle):
    """
    Classe que representa um caminhão, herda de Vehicle.
    """

    def __init__(self, brand, model, year, daily_price):
        """
        Inicializa um novo caminhão.

        :param brand: Marca do caminhão
        :param model: Modelo do caminhão
        :param year: Ano do caminhão
        :param daily_price: Preço diário do aluguel
        """
        super().__init__(brand, model, year, daily_price)

    def display_info(self):
        """
        Exibe informações específicas sobre o caminhão.
        """
        return super().display_info() + " - Caminhão"
