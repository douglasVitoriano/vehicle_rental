from src.config import Config

def format_currency(amount):
    """
    Formata um valor numérico como uma string de moeda.

    :param amount: Valor numérico a ser formatado
    :return: String formatada como moeda
    """
    return f"{Config.CURRENCY} {amount:.2f}"

def validate_vehicle_type(vehicle_type, allowed_types):
    """Valida se o tipo de veículo é permitido"""
    return vehicle_type in allowed_types
