from src.controllers.rental_controller import RentalController

def main():
    """
    Função principal para executar o sistema de aluguel de veículos.
    """
    controller = RentalController()
    
    while True:
        print("\nBem-vindo ao sistema de aluguel de veículos!")
        print("1. Mostrar veículos disponíveis")
        print("2. Alugar um veículo")
        print("3. Devolver um veículo")
        print("4. Sair")
        
        choice = int(input("Escolha uma opção: "))
        
        if choice == 1:
            controller.show_available_vehicles()
        elif choice == 2:
            controller.show_available_vehicles()
            vehicle_choice = int(input("Escolha o número do veículo para alugar: "))
            controller.rent_vehicle(vehicle_choice)
        elif choice == 3:
            controller.show_available_vehicles()
            vehicle_choice = int(input("Escolha o número do veículo para devolver: "))
            controller.return_vehicle(vehicle_choice)
        elif choice == 4:
            print("Obrigado por usar o sistema de aluguel de veículos!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
