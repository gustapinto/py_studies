''' Some function implementation examples'''

# Declare a function with def
def plus(n1, n2):
    return n1 + n2

print(f'Ordered sum = {plus(2, 3)}')  # Call function w/ordered parameters
print(f'Named sum = {plus(n2=6, n1=7.5)}')  # Call function w/named parameters

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
