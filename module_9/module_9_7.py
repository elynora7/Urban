def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 0:
            is_prime = True
            if result != 1:
                for i in range(2, result):
                    if result % i == 0:
                        is_prime = False
                        break
            print('Простое' if is_prime else 'Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
