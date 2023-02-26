from dataclasses import dataclass, field, InitVar, make_dataclass
from pprint import pprint

class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


Cardata = make_dataclass('Cardata', [('model', str),
                                 'max_speed',
                                 ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed})

c = Cardata('Ford', 100, 4096)
print(c)
print(c.get_max_speed())