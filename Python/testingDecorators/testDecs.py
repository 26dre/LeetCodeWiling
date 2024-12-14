
# def stupid_capitals(txt: str):
#     print("Something to be done before the function is run")
#     txt = txt.lower()
#     txt = list(txt)
#     for i, char in enumerate(txt):
#         if i % 2 == 0:
#             txt[i] = char.upper()

#     return ''.join(txt)


import random
import time
from typing import Any, Callable, Generator


def return_basic_lambda(n: int) -> Callable[[int], int]:
    return lambda x: x * n


def print_which_function_running(fn: Callable[[Any], Any]):
    def inner(*args, **kwargs):
        print(f'Running function : {fn.__name__}')
        print(f'\tRunning with arguments : {args, kwargs}')
        print(f'\tFunction call: {fn.__name__} ({args, kwargs})')
        result = fn(*args, **kwargs)
        return result
    return inner


def calculate_time(fn: Callable[[Any], Any]):
    in_prog = False

    def inner(*args, **kwargs):
        nonlocal in_prog
        if not in_prog:
            print("Starting running timer")
            in_prog = True
            start = time.time()
            result = fn(*args, **kwargs)

            end = time.time()

            print(f'Running {fn.__name__} with', end='')
            if len(str(**kwargs)) > 100 or len(str(*args)) > 100:
                print(f'took {end - start} time')
            else:

                print(f'{args, kwargs} took {end - start} time')
            in_prog = False

            return result
        else:
            return fn(*args, **kwargs)
    return inner


def calc_time_not_decor(fn: Callable[[Any], Any], *args, **kwargs) -> Callable[[Any], Any]:
    print("Starting running timer")
    start = time.time()
    _ = fn(*args, **kwargs)

    end = time.time()

    print(f'Running {fn.name} with', end='')
    print(f'{args, kwargs} took {end - start} time')


def shitty_fact(n: int):
    if n == 0:
        return 1
    else:
        return n * shitty_fact(n - 1)


@calculate_time
@print_which_function_running
def shitty_fact_decor(n: int):
    if n == 0:
        return 1
    else:
        return n * shitty_fact_decor(n - 1)


@calculate_time
# @print_which_function_running
def times_wtvr_wrapper(n: int, x: int):
    times_n = return_basic_lambda(n)
    return times_n(x)
# calculate_time(print(shitty_fact(6)))


def my_range(n: int) -> Generator:
    i = 0
    while i < n:
        yield i
        i += 1


def evens(n: int) -> Generator:
    i = 0
    while i < n:
        yield i
        i += 2


class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration

        result = self.i

        self.i += 2
        return result


class MyRange:
    def __init__(self, end, start=0, increment=1):
        self.end = end
        self.start = start
        self.increment = increment

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.start >= self.end:
            raise StopIteration

        res = self.start
        self.start += self.increment

        return res

    def __repr__(self):
        return f'MyRange({self.start}, {self.end}, {self.increment})'


if __name__ == '__main__':

    # thing = calc_time_not_decor(shitty_fact, 500)
    # shitty_fact_decor(6)
    # result = shitty_fact_decor(422)

    # print(f'result = {result}')

    # times_20 = return_basic_lambda(20)
    # print(times_wtvr_wrapper(30, 4))

    # for i in my_range(10):
    #     print(i)

    # x = my_range(10)

    # x = my_range(10)
    # print(f'type = {type(x)}, wtvr = {x}')
    # print(x)

    # x = EvenNumbers(10)
    # for i in x:
    #     print(i)

    # for i in evens(10):
    #     print(i)

    # r = [x**2 for x in evens(10)]
    # other_r = [x for x in EvenNumbers(10)]
    # print(f'r = {r}')
    # print(f'other_r = {other_r}')

    # r = (x**2 for x in evens(10))
    # other_r = (x**3 for x in EvenNumbers(10))
    # print(f'r = {r}')
    # print(f'other_r = {other_r}')

    # for nums in zip(r, other_r):
    #     print(f'nums = {nums}')

    # new_range_obj = MyRange(start=1, end=10, increment=3)
    # for i in new_range_obj:
    #     print(i)
    # print(new_range_obj)
    # for i in MyRange(10, 5, 2):
    #     print(i)

    # i = range(1, 10, 2)
    # print(len(i))

    # l = ['', 11, 2, 23, 14, 5, 'hi', 'hello', 'wtvr', 'stupid']
    # str_l = [x for x in l if isinstance(x, str)]
    # int_l = [x for x in l if isinstance(x, int)]

    # new_dict = {k: v for (k, v) in zip(str_l, int_l)}

    # print(new_dict.items())

    # sorted_dict = sorted(
    #     new_dict.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_dict)

    l = [random.randrange(1, 100, 1) for i in range(10000)]
    # print(l)
    calc_time_sorted = calculate_time(sorted)
    calc_time_sorted(l)
