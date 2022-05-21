from laptop import SouthAmericaLaptop
from power_socket import AmericanSocket, EuropeanSocket

if __name__ == '__main__':
    laptop = SouthAmericaLaptop()

    # I'm in southamerica
    american_socket = AmericanSocket()
    response_laptop_1 = laptop.charge(socket=american_socket, power_socket=190)
    print('America ', response_laptop_1)

    # I'm in Europe
    european_socket = EuropeanSocket()
    response_laptop_2 = laptop.charge(socket=european_socket, power_socket=200)
    print('Europe', response_laptop_2)
