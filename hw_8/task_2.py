def divisors(number):
    number = int(number)
    res = []
    for i in range(1, number + 1):
        if number % i == 0:
            res.append(i)
    return res
