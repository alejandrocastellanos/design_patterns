from time import sleep

from generic_factory import GenericFactory
from mountain_factory import MountainFactory


# Online Store
class BicycleStore:

    def __init__(self, factory):
        instance_factory = factory()
        self.tires = instance_factory.add_tires()
        self.frame = instance_factory.add_frame()


if __name__ == "__main__":

    # main method to call others
    bicycle = {
        'generic': BicycleStore(GenericFactory),
        'mountain': BicycleStore(MountainFactory)
    }

    while True:
        print('-----------')
        print('1) Write the type of bicycle')
        type = input()
        get_type = bicycle.get(type)
        print(f'the bicycle has {get_type.tires.part_type()}')
        print(f'and {get_type.frame.part_type()}')
        sleep(3)
