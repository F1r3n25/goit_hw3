import concurrent.futures
from multiprocessing import cpu_count
from datetime import datetime


def factorize(number):
    return [el for el in range(1, number + 1) if (number % el) == 0]


arguments = (128, 255, 99999, 10651060)

if __name__ == '__main__':
    start = datetime.now().timestamp()
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        a, b, c, d = list(executor.map(factorize, arguments))
    print(datetime.now().timestamp()-start)



    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
