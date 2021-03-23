''' Another simple series of examples about manipulating and class
    formation in Python 3.8
'''

# Defining the main classe
class Foo():
    def __init__(self):  # Class constructor
        pass

# The Bar class has a inheritance on Foo
class Bar(Foo):
    def __init__(self):
        super().__init__()  # The 'super()' get the desired methods from parent class

# Python 3 also supports multiple inheritance
class Foobar(Bar, Foo):
    def __init__(self):
        # Explicit define the desired parents methods instead of using 'super()'
        Foo.__init__(self)
        Bar.__init__(self)

''' Abstract classe cannot be instantied and serves as
    a model, being a generic superclass
'''
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod  # This must be present on every subclass of Abstract()
    def do_something(self):
        pass

class NotSoAbstract(Abstract):
    def do_something():  # Here is ;D
        pass

''' Something interesting: ever class on Python descend from the 'type'
    metaclass
'''
f = Foo()
b = Bar()

print(type(f))  # 'f' type is Foo, but ...
print(type(Foo))  # 'Foo' type is "type", and ....
print(type(type))  # 'type' type is "type".
