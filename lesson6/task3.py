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
