class PowerSocket:

    def __init__(self, hole_num, shape, volt):
        self._num_holes = hole_num
        self._hole_shape = shape
        self._volt = volt

    def get_num_holes(self):
        return self._num_holes

    def get_hole_shape(self):
        return self._hole_shape

    def get_volt(self):
        return self._volt


class ChineseSocket(PowerSocket):

    def __init__(self):
        super().__init__(3, 'flat', 220)


class EuropeanSocket(PowerSocket):

    def __init__(self):
        super().__init__(3, 'cube', 205)


class AmericanSocket(PowerSocket):

    def __init__(self):
        super().__init__(3, 'cube', 210)

