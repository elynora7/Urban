# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    a = 'Абстрактный'
    print(f'1. Длина строки, "{a}" = {len(a)}')  # Press Ctrl+F8 to toggle the breakpoint.

    first = 54
    second = 37
    summa = first + second
    diff = first - second
    print(f'2. Сумма = {summa}, разность = {diff}')

    third = 43
    mean = (first + second + third) / 3
    print(f'3. Среднее арифметическое = {mean}')

    first_string = 'Вторник'
    second_string = 'Понедельник'
    print(f'4. {second_string}, {first_string}')

    a = 2
    b = 3
    c = 4
    f = (a * b) + (a * c)
    print(f'5. {f ** 3 / 2}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
