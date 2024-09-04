from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy_count = 100
        day_count = 0
        while enemy_count > 0:
            enemy_count -= self.power
            day_count += 1
            print(f'{self.name}, сражался {day_count} дней(дня)..., осталось {enemy_count} войнов')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')


first_knight = Knight('Sir Loncelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
