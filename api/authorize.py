banco_de_dados = ["PLL3J74", "PLL2186", "RI02A19"]


def check_if_plate_have_permission(placa: str) -> bool:
    return True if placa in banco_de_dados else False
