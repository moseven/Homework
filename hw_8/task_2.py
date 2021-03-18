def divisors(number):
    number = int(number)
    res = []
    for i in range(1, number + 1):
        if int(number) % int(i) == 0:
            res.append(i)
    return res
