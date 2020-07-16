#some simple function examples

number1 = float(input('Number: '))
number2 = float(input('Another Number: '))

#declaring the function with def
def plus(a, b):
    return a + b

print('Sum = {}'.format(plus(number1, number2))) #call with ordered arguments

def printSomeoneSayingSomething(name, city, state):
    print("Hi there i'm {name}, from {city}-{state}.".format(name=name,city=city,state=state))

printSomeoneSayingSomething('Dave', 'Leme', 'SP') #call with ordered arguments

printSomeoneSayingSomething(city='Araras', name='Carlinhos Brown', state='SP') #call with named arguments

#create a first class function
def firstClassFunction(name1):
    #    The first class fucntion is a function that return
    #    another function, and can be storaged in variables or constants

    def someOtherFunction(name2):
        return print('{name1} != {name2}'.format(name1=name1, name2=name2))

    return someOtherFunction

add_name = firstClassFunction('Josias')
add_name('Cléber')

#creates a anonymous function with lambda
(lambda n1, n2: print('This Sum was done with lambda = {total}'.format(total=n1+n2)))(number1, number2)