from jeep_builder import JeepBuilder

from director import Director


def main():

    jeep_builder = JeepBuilder()

    director = Director()

    # build Jeep
    print('Building jeep...')
    director.set_builder(jeep_builder)
    jeep = director.get_car()
    jeep.specification()
    print('Finished Jeep build')


if __name__ == '__main__':
    main()
