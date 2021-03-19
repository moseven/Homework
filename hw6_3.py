N = int(input('Input number: '))
arr = [i for i in range(2, N + 1)]

for i in arr:
    if i ** 2 <= N:
        if i != 0:
            for j in range(arr.index(i ** 2), len(arr), i):
                arr[j] = 0

arr = [i for i in arr if i != 0]

print(arr)
