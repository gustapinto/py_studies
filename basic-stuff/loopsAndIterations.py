""" A series of simple implementations of loops and iterations

Yeah, the output is just a mess of numbers and words :D
"""

array = [1, 2, 3, 4, 5, 6, 7]
dictionary = {
    'random_key_1': 'something',
    'random_key_2': 'another thing',
    'not_so_random_key_3': 'a thing'
}


# Using the 'for' statement to loop over a range of five numbers,
# generating a arithmetc progressions.
for i in range(5):  # It's like using: (i = 0; i < 5; i++)
    print(i)

for i in range(2, 10, 2): # Using (lower number, upper number, step)
    print(i)


# Using the 'for' statement to iterate...
for element in array:  # Over a list
    print(element)

for key, element in dictionary.items():  # And over a dictionary
    print(f'{key} - {element}')


# The 'for' statement can also be used in a 'for else' way
for i in range(5):
    print(i)
else:
    print('The end')

# The loop sequence can be stopped using the 'break' statement and conditionaly
# continued using the 'continue' statement
for i in range(5):
    if i > 3:
        print('Bye bye babe')
        break
    print(i)

for i in range(5):
    if i % 2 == 0:
        print(f'{i} is a even number')
        continue  # Proceed to next iteration
    print(f'{i} is a odd number')
