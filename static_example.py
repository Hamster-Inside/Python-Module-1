class Aquarium:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def calculate_capacity(self):
        return self.height * self.width * self.depth

    @staticmethod
    def calculate_xy(width, depth):
        return width * depth


aquarium = Aquarium(100, 80, 40)
print(aquarium.calculate_capacity())
print(aquarium.calculate_xy(200, 200))
