"""
#task 1
import itertools
import time


class TrafficLight:
    __color: str
    __timing: dict

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 5):
        self.__timing = {
            "red": red_time,
            "yellow": yellow_time,
            "green": green_time
        }

    def running(self):
        for mode, timer in itertools.cycle(self.__timing.items()):
            self.__color = mode

            for second in range(timer):
                print(f"{self} [{second + 1}]")
                time.sleep(1)

    def __repr__(self):
        return f"Running = {self.__color}"


traffic_light = TrafficLight(7, 2, 5)
traffic_light.running()



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

#task 3
class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


worker1 = Position("Name1", "NameSon", "Transporter", 2000, 1000)
print(worker1.get_full_name(), worker1.get_total_income())

worker2 = Position("Name2", "NameSon2", "PenguinHugger", 10000, 5000)
print(worker2.get_full_name(), worker2.get_total_income())



# task 4

class Car:
    speed: str
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police=False):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.name, 'speed limit')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.name, 'speed limit')


class PoliceCar(Car):
    is_police = True


class SportCar(Car):
    pass


cars = [
    SportCar(240, 'red', 'Audi'),
    TownCar(180, 'silver', 'Kia'),
    WorkCar(80, 'white', 'Golf'),
    PoliceCar(170, 'black', 'Ford'),
]

cars[0].go()
cars[0].turn('rigth')
cars[0].turn('left')
cars[0].stop()

for car in cars:
    print(car.__class__)
    car.show_speed()

"""


# task 5
class Stationery:
    title: str

    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print('draw Parent')


class Pen(Stationery):
    def draw(self):
        print(type(self).__name__, 'draw Pen')


class Pencil(Stationery):
    def draw(self):
        print(type(self).__name__, 'draw Pencil')


class Handle(Stationery):
    def draw(self):
        print(type(self).__name__, 'draw Handle')


myclass1 = Stationery()
myclass1.draw()
myclass2 = Pen()
myclass2.draw()
myclass3 = Pencil()
myclass3.draw()
myclass4 = Handle()
myclass4.draw()
