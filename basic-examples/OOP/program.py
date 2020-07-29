import main as m

dave = m.Human(name = 'Dave', age = 34)
dave.description()

mainframe = m.Computer(brand = 'IBM', cores = 16, ram = 64)
mainframe.review()

dave_from_future = m.NextHuman(name = 'Dave', age = 17)
dave_from_future.description()

cyborg_dave = m.Cyborg(
    name = 'Dave',
    age = 12,
    brand = 'Xiaomi',
    cores = 128,
    ram = 1022
)
cyborg_dave.description()
cyborg_dave.review()