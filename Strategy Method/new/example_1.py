import types


class StrategyExample:

    def __init__(self, func=None):
        self.def_name = 'strategy example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(f'Funcion = {self.def_name}')


def strategy_example_1(self):
    print(f'{self.def_name} ejecutando strategy_example_1 ....')


def strategy_example_2(self):
    print(f'{self.def_name} ejecutando strategy_example_2 ....')


example_0 = StrategyExample()
example_0.execute()

example_1 = StrategyExample(strategy_example_1)
example_1.def_name = 'strategy example 1'
example_1.execute()

example_2 = StrategyExample(strategy_example_2)
example_2.execute()
