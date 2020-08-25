""" Another simple series of examples about manipulating and class
    formation in Python3

    someone: - why the examples ever are simple?
    someone2: - E X A M P L E S dude
"""

# Defining the mian classes
class Foo():
    def __init__(self):
        pass

class Bar(Foo):
    def __init__(self):
        super().__init__()


""" Something interesting: ever class on Python descend from the 'type'
    metaclass
"""
f = Foo()
b = Bar()

print(type(f))  # 'f' type is Foo, but ...
print(type(Foo))  # 'Foo' type is "type", and ....
print(type(type))  # 'type' type is "type".
