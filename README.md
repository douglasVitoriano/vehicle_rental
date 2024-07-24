# Sistema de Locação de Veículos

# 🚗 Vehicle Rental System

## Descrição
Este projeto é um sistema de locação de veículos desenvolvido em Python, utilizando princípios de programação orientada a objetos. Foi criado como parte de um desafio proposto pelos professores da pós-graduação em Machine Learning Engineering na FIAP.

## Funcionalidades
- **Gerenciamento de veículos**: Adicionar, listar e alugar veículos disponíveis na frota.
- **Exibição de detalhes**: Mostrar informações detalhadas sobre os veículos, incluindo marca, modelo, ano e preço por dia.
- **Processo de aluguel**: Alugar veículos e devolvê-los após o uso.
- **Listagem de veículos disponíveis**: Listar veículos disponíveis para aluguel e exibir todos os veículos, incluindo os alugados.

## Estrutura do Projeto

vehicle_rental
├── src
│ ├── main.py: Arquivo principal que integra todas as funcionalidades do sistema e fornece a interface de linha de comando.
│ ├── config.py: Contém configurações do projeto, como informações de moeda.
│ ├── controllers
│ │ ├── init.py
│ │ └── rental_controller.py: Controlador responsável pela interação entre a interface do usuário e o serviço de aluguel.
│ ├── models: Define a classe base `Vehicle` e suas subclasses `Car`, `Motorcycle` e `Truck`.
│ │ ├── init.py
│ │ ├── vehicle.py
│ │ ├── car.py
│ │ ├── motorcycle.py
│ │ └── truck.py
│ ├── services
│ │ ├── init.py
│ │ └── rental_service.py: Serviço que gerencia a lógica de aluguel de veículos e mantém o estado dos veículos.
│ ├── utils
│ │ ├── init.py
│ │ └── helpers.py: Contém funções auxiliares, como a formatação de preços.
├── tests
│ ├── init.py
│ └── test_rental.py: Contém os testes das funcionalidades do projeto
├── requirements.txt
└── README.md


## Como Executar

1. Clone o repositório.

git clone https://github.com/douglasVitoriano/vehicle_rental.git

2. Navegue até o diretório do projeto: 

cd vehicle_rental

3. Execute o arquivo `main.py` para iniciar o programa.

python src/main.py

Contribuidor

- Douglas Augusto Vitoriano | douglas_vitoriano@yahoo.com.br | RM357899
