from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start_func = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_func = datetime.now()
print(f'Работа функций {end_func - start_func}')

start_thread = datetime.now()

thr1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

end_thread = datetime.now()
print(f'Работа потоков {end_thread - start_thread}')
