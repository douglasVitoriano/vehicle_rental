class Vehicle:
    """
    Classe base para todos os tipos de veículos.
    """

    def __init__(self, brand, model, year, daily_price):
        """
        Inicializa um novo veículo.

        :param brand: Marca do veículo
        :param model: Modelo do veículo
        :param year: Ano do veículo
        :param daily_price: Preço diário do aluguel
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_price = daily_price
        self.is_available = True  # O veículo está disponível para aluguel

    def display_info(self):
        """
        Exibe informações do veículo.

        :return: String com as informações do veículo
        """
        return f"Marca: {self.brand}, Modelo: {self.model}, Ano: {self.year}, Preço por dia: {self.daily_price}"

    def rent(self):
        """
        Marca o veículo como alugado.
        """
        self.is_available = False

    def return_vehicle(self):
        """
        Marca o veículo como disponível.
        """
        self.is_available = True
