from threading import Thread
from time import sleep
from datetime import datetime


def decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args)
        print(f'Завершилась запись в файл {args[1]}')
        return result

    return wrapper


@decorator
def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}' + '\n')
            sleep(0.1)


t1_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

t1_end = datetime.now()

print(f'Работа без потоков {t1_end - t1_start}')

t2_start = datetime.now()

first_thread = Thread(target=write_words, args=(10, 'example5.txt'))
second_thread = Thread(target=write_words, args=(30, 'example6.txt'))
third_thread = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_thread = Thread(target=write_words, args=(100, 'example8.txt'))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

t2_end = datetime.now()

print(f'Работа потоков {t2_end - t2_start}')