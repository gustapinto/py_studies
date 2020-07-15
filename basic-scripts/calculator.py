while True:
    first_number = float(input('First number: '))

    print("""
        Accepted operations:
        [+] Sum              [*] Multiplication      [%] Module
        [-] Subtraction      [/] Division            [^] Exponentiation
    """)

    option = input('Option: ')

    accepted_options = ['+', '-', '*', '/', '%', '^', 'h']

    if option in accepted_options:
        second_number = float(input('Second number: '))

        if option == '+':
            total = first_number + second_number
        elif option == '-':
            total = first_number - second_number
        elif option == '*':
            total = first_number * second_number
        elif option == '/':
            total = first_number / second_number
        elif option == '%':
            total = first_number % second_number
        elif option == '^':
            total = first_number ** second_number
        else:
            print('What heck is this ???')
            exit()
    else:
        print('Invalid Option: {inputed_option}. Try again.'.format(inputed_option=option))
        exit()

    print('{number1} {option} {number2} = {total}'.format(number1=first_number, number2=second_number, option=option, total=total))

    answer = input('[yes/no] Run again? ')

    if answer in ('yes', 'no'):
        if answer == 'yes':
            continue
        else:
            exit()
    else:
        print('Invalid Input.')
        exit()
