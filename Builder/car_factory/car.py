from parts import Body, Engine, Wheel


class Car:

    def __init__(self):
        self._wheels = []
        self._engine = None
        self._body = None

    def set_body(self, body: Body):
        self._body = body

    def set_engine(self, engine: Engine):
        self._engine = engine

    def attach_wheel(self, wheel: Wheel):
        self._wheels.append(wheel)

    def specification(self):
        print(f'Body: {self._body.shape}')
        print(f'Engine: {self._engine.horse_power}')
        print(f'Tire size: {self._wheels[0].size}')
