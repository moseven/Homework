num = int(input('Input number: '))
for i in range(num):
    row = ''
    for j in range(num - 1 - i):
        row += ' '
    for k in range(i+1):
        row += '**'
    print(row)