from threading import Thread
from random import randint
import queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        waiting = randint(3, 10)
        sleep(waiting)


class Cafe:
    def __init__(self, *tables_list):
        self.table_list = tables_list
        self.queue = queue.Queue()

    def __have_guests(self):
        ret_count_guests = int()
        for table in self.table_list:
            if table.guest:
                ret_count_guests += 1
        return ret_count_guests

    def guest_arrival(self, *guests):
        guests_list = list(guests)
        table_count = len(self.table_list)
        if self.__have_guests() < table_count:
            for table in self.table_list:
                if not table.guest:
                    guest = guests_list.pop(0)
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    guest.start()
        if self.__have_guests() == table_count:
            for guest in guests_list:
                self.queue.put(guest)

    def discuss_guests(self):
        cycle_run = True
        while cycle_run:
            for table in self.table_list:
                if self.__have_guests() == 0 and self.queue.empty():
                    cycle_run = False
                if table.guest is None and self.queue.empty():
                    continue
                elif table.guest is None and not self.queue.empty():
                    gst = self.queue.get()
                    table.guest = gst
                    table.guest.start()
                    print(f'{gst.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                elif not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
        print('Все покушали, больше никто не пришёл и кафе закрылось')


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
