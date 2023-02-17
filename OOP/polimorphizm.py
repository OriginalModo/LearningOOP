class Room:
    def __init__(self, l=0, w=0):
        self.l = l
        self.w = w

    def get_s(self):
        return self.l * self.w

    def __add__(self, other):
        if isinstance(other, (int,float)):
            return self.get_s() + other
        elif isinstance(other, Room):
            return self.get_s() + other.get_s()
        return 0

class House:
    def __init__(self, *args):
        self.rooms = args
        self.s = 0


    def get_s(self):
        for room in self.rooms:
            self.s += room.get_s()
        return self.s

room1 = Room(2, 3)
room2 = Room(4, 5)
room3 = Room(2, 5)

house = House(room1, room2, room3)
print(house.get_s())


s = room1 + room2 
print(s)