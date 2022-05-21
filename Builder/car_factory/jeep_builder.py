from builder import Builder
from parts import Wheel, Body, Engine


class JeepBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horse_power = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'SUV'
        return body
