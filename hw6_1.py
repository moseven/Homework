while True:
    first_numb = ''

    while not isinstance(first_numb, int):
        try:
            first_numb = int(input('Input number 1: '))
        except ValueError:
            print('Please, input only numbers')

    operation = input('Input operation: ')

    if operation == 'sqrt':
        print(first_numb ** 0.5)
        continue

    second_numb = ''

    while not isinstance(second_numb, int):
        try:
            second_numb = int(input('Input number 2: '))
        except ValueError:
            print('Please, input only numbers')
    try:
        if operation == '+':
            print(first_numb + second_numb)
        elif operation == '-':
            print(first_numb - second_numb)
        elif operation == '*':
            print(first_numb * second_numb)
        elif operation == '/':
            print(first_numb / second_numb)
        elif operation == '**':
            print(first_numb ** second_numb)
        else:
            print('Please, input operations like:  +,-,*,/,**,sqrt')

    except ZeroDivisionError:
        print('Division on zero is impossible')

