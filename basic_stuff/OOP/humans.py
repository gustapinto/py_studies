''' Create the parent classes
'''
class Human:
    species = 'Homo Sapiens Sapiens'
    lifetime = 75

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

class Computer:
    def __init__(self, *args, **kwargs):
        self.brand = kwargs['brand']
        self.cores = kwargs['cores']
        self.ram = kwargs['ram']


''' Create the child classes
'''
class NextHuman(Human):
    species = 'Homo Superior'
    lifetime = Human.lifetime * 2.15

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Cyborg(Human, Computer):
    species = 'Homo Machina'
    lifetime = Human.lifetime * 16

    def __init__(self, *args, **kwargs):
        # Explicit define the __init__(s) instead of using super().Class
        Human.__init__(self, *args, **kwargs)
        Computer.__init__(self, *args, **kwargs)
