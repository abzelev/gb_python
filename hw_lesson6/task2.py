# task 2
class Road:
    _length: float
    _width: float
    __mass: float = 25.0

    def __init__(self, lenth: float, width: float):
        self._length = lenth
        self._width = width

    def road_mass(self, depth: float = 1):
        return (self._length * self._width * self.__mass * depth) / 1000


myRoad = Road(20, 5000)
print(myRoad.road_mass(5))
