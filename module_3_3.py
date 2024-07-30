def print_params(a=1, b='строка', c=True):
    print(f'a = {a}, b = {b}, c = {c}')


print_params()
print_params(3)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [56, 'другая строка', False]
values_dict = {'a': 'Это а', 'b': True, 'c': 756}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)