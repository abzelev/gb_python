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