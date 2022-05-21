# Tires Factory
class GenericTires:

    def part_type(self):
        return 'Generic Tire'


# Frame Factory
class GenericFrame:

    def part_type(self):
        return 'Generic Frame'


# Factory
class GenericFactory:

    def add_tires(self):
        return GenericTires()

    def add_frame(self):
        return GenericFrame()
