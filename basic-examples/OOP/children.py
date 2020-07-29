from parents import Human, Computer

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


dave_from_future = NextHuman(name = 'Dave', age = 17)
dave_from_future.description()

cyborg_dave = Cyborg(
    name = 'Dave',
    age = 12,
    brand = 'Xiaomi',
    cores = 128,
    ram = 1022
)
cyborg_dave.description()
cyborg_dave.review()
