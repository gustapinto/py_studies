"""
    Standard Python library modules and usage.
"""

# Basic import.
import math
print (math.sqrt(64))

# Import a module with a alias.
import math as m
print(m.sqrt(64))

# Import only a part of a module, to the actual namespace.
from math import sqrt
print(sqrt(64))

# Import a module function with a alias.
from math import sqrt as square_root
print(square_root(64))

# Import all the parts of the module to the actual namespace.
from math import *
print(factorial(5))

"""
    Custom module imports and usage.
"""

# The custom modules use all the module options, like:
import modules.customModule
modules.customModule.print_hello()

import modules.customModule as custom
custom.print_hello()

from modules.customModule import print_hello
print_hello()

from modules.customModule import print_hello as hello
hello()

from modules.customModule import *
print_sum(2, 4)