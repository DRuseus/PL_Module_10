import multiprocessing
from datetime import datetime


def read_info(name):
    with open(name, 'r') as file:
        all_data = [line[0:-1] for line in file.readlines() if not line.isspace()]


file_list = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейное вычисление
    start = datetime.now()
    read_info('file 1.txt')
    read_info('file 2.txt')
    read_info('file 3.txt')
    read_info('file 4.txt')
    end = datetime.now()
    print(end - start)
    # 0:00:04.380398

    # Мультипроцессорное вычисление
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, file_list)
    end = datetime.now()
    print(end - start)
    # 0:00:01.683522
