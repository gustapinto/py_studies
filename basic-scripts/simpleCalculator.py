#simple python3 calculator, without any option (aka. if)

#creating a variable and defining its value by input
number1 = int(input('Write the first number: '))
number2 = int(input('Write the second number: '))

#some mathematical operators
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
exponentiation = number1 ** number2

print('')
print(number1, '+', number2, '=', addition)
print(number1, '-', number2, '=', subtraction)
print(number1, 'x', number2, '=', multiplication)
print(number1, '/', number2, '=', division)
print(number1, '^', number2, '=', exponentiation)
