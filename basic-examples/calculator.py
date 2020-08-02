import sys

print('''
|----------------------------------------------------------------|
|                     Accepted operations                        |
|----------------------------------------------------------------|
|  [+] Sum            [*] Multiplication    [%] Module           |
|  [-] Subtraction    [/] Division          [**] Exponentiation  |
|----------------------------------------------------------------|
''')

accepted_operators = ('+', '-', '*', '/', '%', '**')

while True:
    try:
        n1 = float(input('First number: '))
        operator = input('Math operator: ')

        if operator in accepted_operators:
            n2 = float(input('Second number: '))

            total = eval(str(n1) + operator + str(n2))

            print(f"{n1} {operator} {n2} = {total}")
        else:
            print(f'Invalid math operator.')

    except:
        error = sys.exc_info()[0]

        if error == ZeroDivisionError:
            print("Can't divide or module a number by 0.")
        elif error == ValueError:
            print("A letter or a simbol isn't a number.")
        else:
            print(f'Error code: {error}')

    answer = input('\n[yes/no] Run again? ')

    if answer in ('yes', 'y'):
        print('')

        continue
    else:
        print('Goodbye.')

        break
