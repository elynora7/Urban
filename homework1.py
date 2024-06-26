
def lesson1():
    example = 'Абстрактный'
    print(f'{example[0]}')
    print(f'{example[-1]}')
    print(f'{example[len(example) // 2:]}')
    print(f'{example[::-1]}')
    print(f'{example[1::2]}')


if __name__ == '__main__':
    lesson1()

