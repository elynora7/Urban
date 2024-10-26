import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            s = randint(50, 500)
            self.balance += s
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {s}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            s = randint(50, 500)
            print(f'Запрос на {s}')
            if s > self.balance:
                self.lock.acquire()
                print('Запрос отклонён, недостаточно средств')
            else:
                self.balance -= s
                print(f'Снятие: {s}. Баланс: {self.balance}')

            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
