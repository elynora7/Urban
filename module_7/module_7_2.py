def custom_write(file_name, strings):
    results = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, string in enumerate(strings):
        pos = file.tell()
        file.write(f'{string}\n')
        results[(i + 1, pos)] = string

    file.close()
    return results


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
