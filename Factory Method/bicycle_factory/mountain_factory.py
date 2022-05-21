# Tires Factory
class RuggedTires:

    def part_type(self):
        return 'Mountain Tire'


# Frame Factory
class RuggedFrame:

    def part_type(self):
        return 'Mountain Frame'


# Factory
class MountainFactory:

    def add_tires(self):
        return RuggedTires()

    def add_frame(self):
        return RuggedFrame()
