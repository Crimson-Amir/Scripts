import copy

class ProtoType:
    def __init__(self):
        self._copy_objects = {}

    def register(self, name, value):
        self._copy_objects.setdefault(name, value)

    def unregister(self, name):
        del self._copy_objects[name]

    def make_clone(self, name, **kwargs):
        make_copy = copy.deepcopy(self._copy_objects.get(name))
        make_copy.__dict__.update(**kwargs)
        return make_copy


def client(name, obj, **kwargs):
    instance = ProtoType()
    instance.register(name, obj)
    clone = instance.make_clone(name, **kwargs)
    return clone


class October:
    def __init__(self):
        self.name = 'amir'
        self.age = 24


ins = October()

i1 = client('instance_1', ins)

print(i1.__dict__)