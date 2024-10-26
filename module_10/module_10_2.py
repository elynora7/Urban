import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.warriors = 100
        self.day_count = 0

    def run(self):
        print(f'{self.name} на нас напали!')
        self.battle()
        print(f'{self.name} одержал победу спустя {self.day_count} дней(дня)!')

    def battle(self):
        while self.warriors:
            self.warriors -= self.power
            time.sleep(1)
            self.day_count += 1
            print(f'{self.name} сражается {self.day_count} день(дня)..., осталось {self.warriors} воинов. ')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
