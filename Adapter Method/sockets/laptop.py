from power_socket import PowerSocket
from colombia_plug import Colombia3PingPlug


class SouthAmericaLaptop:

    def __init__(self):
        self.plug = Colombia3PingPlug()

    def charge(self, socket: PowerSocket, power_socket: int):
        res = (self.plug.pins == socket.get_num_holes()) and \
              (self.plug.volt == socket.get_volt()) and \
              (self.plug.pin_shape == socket.get_hole_shape())
        print('res', res)
        if res:
            current = round(power_socket / self.plug.volt, 2)
            return f'Start charging... Power {power_socket} watt; Socket current {current} ...'

        if self.transform_voltage(socket.get_volt()):
            return f'Start charging... Power {power_socket} watt; Socket transform voltage {socket.get_volt()} ...'

        return 'Socket and plug not compatible, impossible to charge.'

    def transform_voltage(self, volt):
        if volt in range(150, 210):
            return True
