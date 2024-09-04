from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    def __init__(self, __balance=0):
        self.__balance = __balance
        self.__lock = Lock()

    def deposit(self):
        for trans in range(100):
            r_int = randint(50, 500)
            self.__balance += r_int
            if self.__balance >= 500 and self.__lock.locked():
                self.__lock.release()
            print(f'Пополнение: {r_int}. Баланс: {self.__balance}')
            sleep(0.01)

    def take(self):
        for trans in range(100):
            r_int = randint(50, 500)
            print(f'Запрос на {r_int}')
            if r_int <= self.__balance:
                self.__balance -= r_int
                print(f'Снятие: {r_int}. Баланс: {self.__balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.__lock.acquire()
            sleep(0.01)

    def get_balance(self):
        return self.__balance


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.get_balance()}')