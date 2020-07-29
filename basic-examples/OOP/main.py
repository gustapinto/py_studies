'''
    Create the parent classes
'''

# Creates the main class for human race.
class Human:

    species = 'Homo Sapiens Sapiens'
    lifetime = 75

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

    def description(self):
        print("{name} is a {age} years old {species}, the expected lifetime is {lifetime} years".format(
            name = self.name,
            age = self.age,
            species = self.species,
            lifetime = self.lifetime
        ))

class Computer:

    architecture = 'ARM'

    def __init__(self, *args, **kwargs):
        self.brand = kwargs['brand']
        self.cores = kwargs['cores']
        self.ram = kwargs['ram']

    def review(self):
        print("The {brand} have {ram}GB of ram and {cores} cores".format(
            brand = self.brand,
            ram = self.ram,
            cores = self.cores
        ))

'''
    Create the child classes
'''

# Create a simple inheritance child class based on Human.
class NextHuman(Human):

    species = 'Homo Superior'
    lifetime = Human.lifetime * 2.15

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Overriding the description method
    def description(self):
        print("{name} is a {age} years old {species}, the expected lifetime is {lifetime} cyber-years".format(
            name = self.name,
            age = self.age,
            species = self.species,
            lifetime = self.lifetime
        ))

# Create a not so simple multiple inheritance class.
class Cyborg(Human, Computer):

    species = 'Homo Machina'
    lifetime = Human.lifetime * 16

    def __init__(self, *args, **kwargs):
        # Explicit define the __init__(s) instead of using super().Class
        Human.__init__(self, *args, **kwargs)
        Computer.__init__(self, *args, **kwargs)

    def review(self):
        print("The {name} have {ram}GB of ram and {cores} cores and is produced by {brand}".format(
            brand = self.brand,
            ram = self.ram,
            cores = self.cores,
            name = self.name
        ))
