from src.services.rental_service import RentalService
from src.models.car import Car
from src.models.motorcycle import Motorcycle
from src.models.truck import Truck
from src.utils.helpers import format_currency

class RentalController:
    """
    Controlador para operações de aluguel de veículos.
    """

    def __init__(self):
        """
        Inicializa o controlador com um serviço de aluguel.
        """
        self.rental_service = RentalService()

        # Adiciona veículos de exemplo
        self.rental_service.add_vehicle(Car("Toyota", "Corolla", 2020, 50, 4))
        self.rental_service.add_vehicle(Motorcycle("Honda", "CB500", 2019, 30))
        self.rental_service.add_vehicle(Truck("Volvo", "FH", 2018, 100))

    def show_available_vehicles(self):
        """
        Exibe os veículos disponíveis para aluguel.
        """
        available_vehicles = self.rental_service.list_available_vehicles()
        for i, vehicle in enumerate(available_vehicles):
            print(f"{i+1}. {vehicle.display_info()}")

    def show_all_vehicles(self):
        """
        Exibe todos os veículos, incluindo os alugados.
        """
        all_vehicles = self.rental_service.list_all_vehicles()
        for i, vehicle in enumerate(all_vehicles):
            print(f"{i+1}. {self.rental_service.display_vehicle_info(vehicle)} {'(Alugado)' if not vehicle.is_available else ''}")

    def rent_vehicle(self, choice):
        """
        Aluga um veículo com base na escolha do cliente.

        :param choice: Índice do veículo escolhido
        """
        available_vehicles = self.rental_service.list_available_vehicles()
        selected_vehicle = available_vehicles[choice - 1]
        if self.rental_service.rent_vehicle(selected_vehicle):
            print(f"Você escolheu alugar: {self.rental_service.display_vehicle_info(selected_vehicle)}")
            # print(f"Você escolheu alugar: {selected_vehicle.display_info()}")
            print("Veículo alugado com sucesso!")
        else:
            print("Desculpe, este veículo não está disponível.")

    def return_vehicle(self, choice):
        """
        Devolve um veículo com base na escolha do cliente.

        :param choice: Índice do veículo a ser devolvido
        """
        available_vehicles = self.rental_service.list_available_vehicles()
        selected_vehicle = available_vehicles[choice - 1]
        self.rental_service.return_vehicle(selected_vehicle)
        print("Veículo devolvido com sucesso!")

    def _format_vehicle_info(self, vehicle):
        """
        Formata as informações do veículo para exibição.

        :param vehicle: Objeto do veículo
        :return: String formatada com informações do veículo
        """
        return f"Marca: {vehicle.brand}, Modelo: {vehicle.model}, Ano: {vehicle.year}, Preço por dia: {format_currency(vehicle.daily_rate)}"
