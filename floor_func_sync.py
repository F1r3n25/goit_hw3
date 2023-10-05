from datetime import datetime


def timer(func):
    def inner(*args):
        timer_start = datetime.now().timestamp()
        result = func(*args)
        print("Executing time: ", round((datetime.now().timestamp()) - timer_start, 7))
        return result
    return inner


@timer
def factorize(*numbers):
    number_one = [el for el in range(1, numbers[0] + 1) if (numbers[0] % el) == 0]
    number_two = [el for el in range(1, numbers[1] + 1) if (numbers[1] % el) == 0]
    number_three = [el for el in range(1, numbers[2] + 1) if (numbers[2] % el) == 0]
    number_four = [el for el in range(1, numbers[3] + 1) if (numbers[3] % el) == 0]
    return number_one, number_two, number_three, number_four


if __name__ == '__main__':
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
             1521580, 2130212, 2662765, 5325530, 10651060]
