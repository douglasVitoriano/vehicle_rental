from .vehicle import Vehicle

class Motorcycle(Vehicle):
    """
    Classe que representa uma moto, herda de Vehicle.
    """

    def __init__(self, brand, model, year, daily_price):
        """
        Inicializa uma nova moto.

        :param brand: Marca da moto
        :param model: Modelo da moto
        :param year: Ano da moto
        :param daily_price: Preço diário do aluguel
        """
        super().__init__(brand, model, year, daily_price)

    def display_info(self):
        """
        Exibe informações específicas sobre a moto.
        """
        return super().display_info() + " - Moto"
