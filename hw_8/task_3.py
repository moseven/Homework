def my_func(str1):
    dig = []
    let = []
    res = ''
    flag = False
    for i in str1:
        if i.isdigit():
            if flag:
                dig[len(dig) - 1] += i
            else:
                dig.append(i)
            flag = True
        else:
            let.append(i)
            flag = False

    for i in range(len(let)):
        res += let[i] * int(dig[i])
    return res


if __name__ == '__main__':

    file = open('inside.txt', 'r').read().splitlines()
    file2 = open('outside.txt', 'w')

    for line in file:
        file2.write((my_func(line)) + '\n')
    file2.close()
