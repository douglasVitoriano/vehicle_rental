from src.config import Config
from src.utils.helpers import format_currency

class RentalService:
    """
    Serviço de aluguel de veículos.
    """

    def __init__(self):
        """
        Inicializa o serviço de aluguel com uma lista de veículos.
        """
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Adiciona um veículo à lista de veículos disponíveis.

        :param vehicle: Instância de Vehicle a ser adicionada
        """
        self.vehicles.append(vehicle)

    def list_available_vehicles(self):
        """
        Lista todos os veículos disponíveis para aluguel.

        :return: Lista de veículos disponíveis
        """
        return [vehicle for vehicle in self.vehicles if vehicle.is_available]

    def rent_vehicle(self, vehicle):
        """
        Aluga um veículo se estiver disponível.

        :param vehicle: Instância de Vehicle a ser alugada
        :return: True se o aluguel for bem-sucedido, caso contrário, False
        """
        if vehicle.is_available:
            vehicle.rent()
            return True
        return False

    def return_vehicle(self, vehicle):
        """
        Devolve um veículo, marcando-o como disponível.

        :param vehicle: Instância de Vehicle a ser devolvida
        """
        vehicle.return_vehicle()
    
    def display_vehicle_info(self, vehicle):
        """
        Formata e exibe as informações do veículo.

        :param vehicle: Instância de Vehicle
        :return: String formatada com informações do veículo
        """
        return f"Marca: {vehicle.brand}, Modelo: {vehicle.model}, Ano: {vehicle.year}, Preço por dia: {format_currency(vehicle.daily_price)}"