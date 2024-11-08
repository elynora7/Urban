import threading
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for readline in f:
            all_data.append(readline)


filenames = [f'file {number}.txt' for number in range(1, 5)]

# time_start = datetime.now()
# for filename in filenames:
#     read_info(filename)
# time_end = datetime.now()
# print(f'{time_end - time_start} (линейный)')

# time_start = datetime.now()
# threads = {}
# for number in range(4):
#     f = filenames[number]
#     threads[number] = threading.Thread(target=read_info, args=(f,))
# for key, thread in threads.items():
#     thread.start()
# for key, thread in threads.items():
#     thread.join()
# time_end = datetime.now()
# print(f'{time_end - time_start} (линейный)')

if __name__ == '__main__':
    time_start = datetime.now()
    processes = {}
    for number in range(4):
        f = filenames[number]
        processes[number] = multiprocessing.Process(target=read_info, args=(f,))
    for key, process in processes.items():
        process.start()
    for key, process in processes.items():
        process.join()
    time_end = datetime.now()
    print(f'{time_end - time_start} (многопроцессный)')
