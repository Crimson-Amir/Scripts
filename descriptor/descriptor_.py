

class Ten:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = None


class Age:
    person_1 = 5
    person_2 = Ten()


    def __init__(self, p1, p2):
        self.person_1 = p1
        self.person_2 = p2


a = Age('amir', 'ali')

a.person_1 = 2
print(Age.__dict__)
Age.person_2 = 5
print(Age.__dict__)