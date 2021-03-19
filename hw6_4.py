while True:
    year = ''
    while not isinstance(year, int):
        try:
            year = int(input('Input a year: '))
        except ValueError:
            print('Please, input only numbers')
    if year % 4 != 0:
        print('Year is low, 365 days)')
    elif year % 100 != 0 and year % 400 == 0:
        print('Year is leap, 366 days')
    else:
        print('Year is low, 365 days')
