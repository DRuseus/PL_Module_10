import multiprocessing
from datetime import datetime
from threading import Thread


def read_info(name):
    with open(name, 'r') as file:
        all_data = []
        file.seek(0)
        while True:
            line = file.readline().rstrip('\n')
            if not line:
                break
            all_data.append(line)
            print(line)

        """for line in file.readlines():
            if not line.isspace():
                print(line.rstrip('\n'))
                all_data.append(line.rstrip('\n'))"""

        """all_data = [line.rstrip('\n') for line in file.readlines() if not line.isspace()]"""  # Это если не печатать


file_list = (
    'file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'
)

thread_1 = Thread(target=read_info, args=(file_list[0], ))
thread_2 = Thread(target=read_info, args=(file_list[1], ))
thread_3 = Thread(target=read_info, args=(file_list[2], ))
thread_4 = Thread(target=read_info, args=(file_list[3], ))

if __name__ == '__main__':
    # Линейное вычисление
    start_0 = datetime.now()
    read_info('file 1.txt')
    read_info('file 2.txt')
    read_info('file 3.txt')
    read_info('file 4.txt')
    end_0 = datetime.now()

    # Мультипроцессорное вычисление
    with multiprocessing.Pool(processes=4) as pool:
        start_1 = datetime.now()
        pool.map(read_info, file_list)
    end_1 = datetime.now()

    # Просто для сравнение Мултипоточное вычисление
    start_2 = datetime.now()
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    end_2 = datetime.now()

    # Вывод времени вычислений
    print(end_0 - start_0)
    print(end_1 - start_1)
    print(end_2 - start_2)
