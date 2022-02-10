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