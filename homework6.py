my_dict = {'name': 'Ivan',
           'age': 32}
print(my_dict)
print(my_dict.get('name', 'имя не указано'), my_dict.get('last_name', 'фамилия не указана'))
my_dict['last_name'] = 'Petrov'
my_dict['phone_number'] = 89999991234
print(my_dict.pop('phone_number'))
print(my_dict)

my_set = {1, 2, 'String', 2, False, 'String'}
print(my_set)
my_set.add(3)
my_set.add('3')
my_set.discard(2)
print(my_set)
