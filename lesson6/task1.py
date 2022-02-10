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