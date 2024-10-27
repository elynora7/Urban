import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 40))


class Cafe:
    def __init__(self, *tables):
        self.tables = {'empty': list(tables), 'busy': []}
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            if self.tables['empty']:
                table = self.tables['empty'].pop(0)
                table.guest = guest
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
                guest.start()
                self.tables['busy'].append(table)
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while self.tables['busy'] or not self.queue.empty():
            if self.tables['busy']:
                table = self.tables['busy'].pop(0)
                if table.guest and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    self.tables['empty'].append(table)
            if self.tables['empty'] and not self.queue.empty():
                guest = self.queue.get()
                table = self.tables['empty'].pop(0)
                table.guest = guest
                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                guest.start()
                self.tables['busy'].append(table)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
