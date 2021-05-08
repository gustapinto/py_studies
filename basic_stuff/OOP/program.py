import humans as h

class ShowDescriptionSystem:
    def description(self, humans):
        print('      Human Variations on 2212 A.C.      ')
        print('=========================================')
        for human in humans:
            if human.species == 'Homo Machina':
                print(f'{human.name} - {human.species} - from {human.brand} - {human.cores} cores - {human.ram} GB of ram - {human.lifetime} lifespan years')
            else:
                print(f'{human.name} - {human.species} - {human.age} years old - {human.lifetime} lifespan years')


dave = h.Human(name = 'Dave', age = 34)
dave_from_future = h.NextHuman(name = 'Dave', age = 17)
cyborg_dave = h.Cyborg(
    name = 'Dave',
    brand = 'IBM',
    age = 12,
    cores = 128,
    ram = 1022
)
desc_system = ShowDescriptionSystem()
desc_system.description([
    dave,
    dave_from_future,
    cyborg_dave
])

try:
    anonymous = m.NotSoAbstract(id = 12)
except:
    print("<ERROR> You can't do this with a ABSTRACT Class")
