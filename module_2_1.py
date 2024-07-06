print('Hi, PyCharm')
x = 43
y = 32
print(x * y)
print("End line")

numbers = [1, 2, 3, 4, 5]
primes = []
not_primes = []
for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
print(primes)
print(not_primes)
