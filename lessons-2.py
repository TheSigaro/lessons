import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


def input_array():
    num_array = list()
    num = input("Enter how many elements you want:")
    print('Enter numbers in array: ')
    for i in range(int(num)):
        n = input("num :")
        num_array.append(int(n))
    return num_array


@timeit
def match(*args, simple=False, even=False, odd=False):
    arr = args
    if simple:
        for num in arr:
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime and (num != 1):
                print(num)
    if even:
        for num in arr:
            if (num % 2 == 0):
                print(num)
    if odd:
        for num in arr:
            if (num % 2 != 0):
                print(num)


def power(a, p):
    return a ** p


def count_values(counter, *args, step=2, as_list=False):
    # print(counter)
    # print(args)
    if as_list:
        return [counter(v, step) for v in args]
    return {v: counter(v, step) for v in args}


def main():
    print("Hello main!")
    arr = input_array()
    print('With v')
    res = count_values(power, *arr, step=3)
    print(res)
    print('Without v')
    res = count_values(power, *arr, step=3, as_list=True)
    print(res)
    print('Match')
    match(*arr, simple=True)


main()
