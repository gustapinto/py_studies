firstNumber = float(input('First number: '))

print("""
    Accepted operations:
    [+] Sum              [*] Multiplication      [%] Module
    [-] Subtraction      [/] Division            [^] Exponentiation
""")

option = input('Option: ')

acceptedOptions = ['+', '-', '*', '/', '%', '^']

if option in acceptedOptions:
    secondNumber = float(input('Second number: '))

    if option == '+':
        total = firstNumber + secondNumber
    elif option == '-':
        total = firstNumber - secondNumber
    elif option == '*':
        total = firstNumber * secondNumber
    elif option == '/':
        total = firstNumber / secondNumber
    elif option == '%':
        total = firstNumber % secondNumber
    elif option == '^':
        total = firstNumber ** secondNumber
    else:
        print('What heck is this ???')
        exit()
else:
    print('Invalid Option: {inputedOption}. Try again.'.format(inputedOption=option))
    exit()

print('{number1} {option} {number2} = {total}'.format(number1=firstNumber, number2=secondNumber, option=option, total=total))
