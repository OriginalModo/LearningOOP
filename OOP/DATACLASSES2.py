from dataclasses import dataclass, field, InitVar
from pprint import pprint
from typing import Any, Dict, List, Optional, Tuple, Union

class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0,0,0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        print("Book: post_init")
        super().__post_init__()


b = Book(1000,100, 'OOP', 'tupoe')
print(b)