from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self. reliability = reliability

    def drive(self, distance):
        random = randint(0, 101)
        if random >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
