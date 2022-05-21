from builder import Builder
from car import Car


class Director:

    _builder = None

    def set_builder(self, builder: Builder):
        self._builder = builder

    # assembly line
    def get_car(self):
        car = Car()

        # first step
        body = self._builder.get_body()
        car.set_body(body)

        # second step
        engine = self._builder.get_engine()
        car.set_engine(engine)

        # last step
        for _ in range(4):
            wheel = self._builder.get_wheel()
            car.attach_wheel(wheel)

        return car
