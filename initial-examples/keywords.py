''' A basic review on some of Python 3 keywords

    What is a keyword?
    - Keywords are reserved words that have a specific mean and purpose on
      programming languages.
'''

''' Value Keywords (True, False, None)'''

# Python 3 use True, False and None to determine values
x = 1

print(x == 1)  # This will return a True
print(x == 3)  # And this a False, this is a really boring example ;-;

x = None  # Define 'x' as a null value

print(x == None)  # Again a True ...
print(x == 1)  # And a False

y = "Some value, that can be a string or a number"

print(bool(y))  # Python consider any filled variable as a Trulhy result
print(y == True)  # But dont on a explicit comparation

''' Operator keywords (and, or, not, in, is) '''

n1 = 1
n2 = 2

# The 'and' is used to determine if both operands are True
if n1 == 1 and n2 == 2:
    print('Both Ok')

if n1 == 1 and n2 == 3:
    print('This wont work babe')

# The 'or' is used to determine if at least one of the operands are True
if n1 == 1 or n2 == 2:
    print('This will work')

if n1 == 1 or n2 == 3:
    print('This too')

# The 'not' is used to get the opposite boolean of a value
val = False

print(not val)  # The False var returns a True

# The 'in' is used as a containment check
name = 'Clébinho'
n_list = [1, 2, 3, 4, 5]

print('C' in name)  # Checks if 'C' exists in the string
print(3 in n_list)  # This work w/all data structures that can be iterated over

# The 'is' keyword is a identity check, it determines wheter two objects
# are exactly the same, much like the '==='
obj = None
obj2 = ""

print(obj is obj)  # Returns a True
print(obj is None)  # Another True
print(obj2 is obj)  # And a False, because None type is != from "" type

''' Control flow keywords (if, elif, else) '''
true_val = True

# 'if' starts a conditional statement
if true_val:
    print('True')
# The 'elif' acts like a normal 'if' and is used when the 'if' returns a False
elif not true_val:
    print('False')
# 'else' is the last operator of a conditional block,
# and is used when everthing else returns False
else:
    pass

# In Python we use the traditional if/else to create a ternary operator
# ternary sintax: [on_true] if [expression] else [on_false]
print('True') if true_val else print('False')
