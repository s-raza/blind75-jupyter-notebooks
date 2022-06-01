from timeit import default_timer as timer
import datetime
from functools import wraps
import random


def report_time(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = timer()
        ret_val = f(*args, **kwargs)
        end = timer()
        msg = f'{f.__name__} Done in time {str(datetime.timedelta(seconds=end-start))}'
        print(msg)
        print(f"{'='*len(msg)}\n")
        return ret_val

    return wrapper


def print_m(a, func=None, *args, **kwargs):

    print('\nORIGINAL\n')
    for row in a:
        print(row)

    print()

    if func is not None:
        print('TRANSFORMED\n')
        for row in func(a, *args, **kwargs):
            print(list(row))

    print()


def rotate_zip(arr, clockwise=True):

    if clockwise is True:
        return list(zip(*arr[::-1]))
    else:
        return list(zip(*arr))[::-1]


def rotate_matrix(arr, direction=1):

    def rotate(temp_arr, clockwise=True):

        temp_rotated = []

        for i in range(len(temp_arr[0])):

            if clockwise is True:
                idx = i
                rows = temp_arr[::-1]
            else:
                idx = -i-1
                rows = temp_arr

            temp_rotated.append([row[idx] for row in rows])

        return temp_rotated

    rotated = list(arr)

    rotations = abs(direction)

    if rotations % 4 == 0:
        return arr

    rotations = rotations % 4

    clockwise = True if direction > 0 else False

    if rotations % 3 == 0:

        clockwise = not clockwise
        rotations = 1

    for _ in range(rotations):

        rotated = list(rotate(rotated, clockwise))

    return rotated


@report_time
def solve(problems, func_, *args, **kwargs):

    print(f'=={func_.__name__}==\n')

    checker = kwargs.get("checker_func")

    for sno, prob in enumerate(problems):

        inputs = prob[0]
        ans = prob[1]

        if checker is None:
            print(f' {sno+1}- Problem Inputs: {inputs}')
            sol = func_(*inputs, *args, **kwargs)
            print(f'   Solution: {sol}')
            print(f'   Answer: {ans}')
            if not isinstance(sol, list) and isinstance(ans, list):
                print(f' Success: {sol in ans}\n')
            else:
                result = sol == ans
                print(u"\u001b[42;1m PASSED \u001b[0m" if result is True else u"\u001b[41;1m FAIL \u001b[0m")
                print()
        else:
            printer = kwargs.get("printer_func")
            print(f' {sno+1}- Problem Inputs: {inputs}')
            sol = func_(*inputs)
            print("   Solution: ", end="", flush=True)
            printer(sol)
            print("   Answer: ", end="", flush=True)
            printer(ans)
            # print(f' Success: {checker(sol, ans)}\n')
            result = sol == ans
            print(u"\u001b[42;1m PASSED \u001b[0m" if result is True else u"\u001b[41;1m FAIL \u001b[0m")
            print()


def random_list(num_items, start=1, end=10000):

    if num_items > end:
        end = 10000

    list_ = [i for i in range(start, end+1)]

    return random.sample(list_, k=num_items)


def random_dict(num_items, start=1, end=10000):

    list_ = random_list(num_items, start, end)

    return {i: str(i) for i in list_}


def list_counts_dict(list_):

    import collections

    ret_dict = {}
    occ = collections.Counter(list_)

    for item, count in occ.items():

        ret_dict.setdefault(count, []).append(item)

    return ret_dict


def exec_(func, *args):

    print(f"{args}: {func(*args)}\n")


def tointarr(s):

    return [int(i) for i in s.strip("\n").split(" ")]
