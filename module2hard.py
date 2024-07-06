for n in range(3, 21):
    sum = 0
    result = []
    for i in range(1, n):
        for j in range(i + 1, n):
            sum = i + j
            if n % sum == 0:
                result.append(i)
                result.append(j)
    print(f'{n} - ', *result)
