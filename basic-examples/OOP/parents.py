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


dave = Human(name = 'Dave', age = 34)
dave.description()

mainframe = Computer(brand = 'IBM', cores = 16, ram = 64)
mainframe.review()
