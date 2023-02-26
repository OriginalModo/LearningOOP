from dataclasses import dataclass, field, InitVar
from pprint import pprint

class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_length: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_length else 0



@dataclass(frozen=True)
class V3d:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)


v = V3d(1, 2, 3)
