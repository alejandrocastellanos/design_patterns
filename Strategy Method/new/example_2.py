class Uber:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        discount = self.discount_strategy(self) if self.discount_strategy else 0
        return self.price - discount


def standard_vehicle(self):
    return self.price * 14 - 1000


def taxi_vehicle(self):
    return self.price * 12 - 3000


def bus(self):
    return self.price * 5 - 3000


class TotalByVehicle:

    def __init__(self, price):
        self.price = price

    def uber_standar(self):
        uber_standar = Uber(price=self.price, discount_strategy=standard_vehicle)
        return uber_standar.price_after_discount()

    def uber_taxi(self):
        taxi_vehicle_standar = Uber(price=self.price, discount_strategy=taxi_vehicle)
        return taxi_vehicle_standar.price_after_discount()

    def uber_bus(self):
        bus = Uber(price=self.price, discount_strategy=taxi_vehicle)
        return bus.price_after_discount()

    def total(self):
        return f'Uber price = {self.uber_standar()}, Taxi price = {self.uber_taxi()}'


total_by_vehicle = TotalByVehicle(50000)
print(total_by_vehicle.total())
