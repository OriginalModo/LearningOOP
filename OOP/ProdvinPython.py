class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.name + " " + self.last_name

class Author(User):
    def __init__(self, name, last_name, age, article):
        super().__init__(name, last_name, age)
        self.article = article

    def __del__(self):
        return self.name + " " + self.last_name + " " + 'deleted'

    @classmethod
    def age(cls, age):
        if age >= 18:
            return True
        else:
            return False

    @staticmethod
    def boolenval(boolenvalue):
        return boolenvalue

author = Author('Oleksandr', 'Lenart', 21, 15)
print(Author.age(20))




