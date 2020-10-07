""" Some function implementation examples """

# Declare a function with def
def plus(n1, n2):
    return n1 + n2

# Create a first class function
# The first class function returns another function
def first_class_function(name1):
    def function_inside_function(name2):
        comparator = "!="

        if (name1 == name2):
            comparator = "="

        return print(f'{name1} {comparator} {name2}')

    return function_inside_function

# The first class functions can be storaged in variables
compare_names = first_class_function(name1='Josias')
compare_names(name2='Cléber')
compare_names(name2='Josias')

# Creates a anonymous function with lambda
(lambda n1, n2: print(f'This Sum was done with lambda = {n1 + n2}'))(2, 4)

# Lambda functions can also be inserted into variables
lambda_in_a_var = lambda n1, n2: print(f'Lambda in a var sum = {n1 + n2}')
lambda_in_a_var(4, 5)

""" Dealing with arguments """

# Python functions can deal with positional or named arguments
print(f'Ordered sum = {plus(2, 3)}')  # Call function w/positional parameters
print(f'Named sum = {plus(n2=6, n1=7.5)}')  # Call function w/named parameters

# The positional only and keyword only arguments can be marked with a '/,'
# and '*,' respectively on the function definition
def combined_function(positional_only, /, positional_or_keyword,
                      *, keyword_only):
    return print(f'{positional_only}, {positional_or_keyword}, {keyword_only}')

combined_function(11, 12, keyword_only=13)  # Or...
combined_function(11, positional_or_keyword=12, keyword_only=13)

# We can also define functions that can take a variable number of arguments
def args_function(*args):
    # The positional arguments are defined with *, with the name *args being
    # just a convention
    return print(args)  # The arguments are treated like a tuple.

def kwargs_function(**kwargs):
    # The named arguments are defined with **, with the name **kwargs being
    # just a convention
    return print(kwargs)  # The arguments are treated like a dictionary

args_function(1, 2, 3)
kwargs_function(key1=1, key2=2, key3=3)
