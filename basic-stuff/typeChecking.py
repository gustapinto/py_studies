'''
    Some examples to get started with python type checking and hinting
'''

# Dynamic typed var, the python standard
dynamic_var = "something"
print(type(dynamic_var)) # checks the type of the desidered data

dynamic_var = 123 # now changing the string to a int
print(type(dynamic_var))

'''
    Duck typing: the type of a parameter doesn't matter if it does exactly
    what it seems to do.

    "If it walks like a duck, and it quacks like a duck, then it must be a duck"
                                                                 ~ KNOW, i don't
'''
def print_quack(text): # the type of quack doesn't matter
    print('Quack: {quack} {type}'.format(
        quack = text,
        type = type(text)
    ))

print_quack("Quack bro")
print_quack(3.14159265359)
print_quack(404)

'''
    Type hints: sometimes it's really easier to debug if you know the type of
    the goddamn parameter.
'''
def the_virgin_sum(a, b): # aka. without type hints
    print(a + b) # what heck is 'a, b'? strings? ints? some kind of alien code?

the_virgin_sum('2', '3') # useless calls, part. 1
the_virgin_sum(2, 2)

def the_chad_sum(a: float, b: int) -> float: # hint the types
    print(a + b) # dude, it's easy as hell to debug the return

the_chad_sum(23.5, 12) # useless calls, part. 2
