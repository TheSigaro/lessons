import time
import sys
from functools import wraps

class TraceCalls(object):
    """ Use as a decorator on functions that should be traced. Several
        functions can be decorated - they will all be indented according
        to their call depth.
    """
    def __init__(self, stream=sys.stdout, indent_step=2, show_ret=False):
        self.stream = stream
        self.indent_step = indent_step
        self.show_ret = show_ret

        # This is a class attribute since we want to share the indentation
        # level between different traced functions, in case they call
        # each other.
        TraceCalls.cur_indent = 0

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            indent = ' ' * TraceCalls.cur_indent
            argstr = ', '.join(
                [repr(a) for a in args] +
                ["%s=%s" % (a, repr(b)) for a, b in kwargs.items()])
            self.stream.write('%s%s(%s)\n' % (indent, fn.__name__, argstr))

            TraceCalls.cur_indent += self.indent_step
            ret = fn(*args, **kwargs)
            TraceCalls.cur_indent -= self.indent_step

            if self.show_ret:
                self.stream.write('%s--> %s\n' % (indent, ret))
            return ret
        return wrapper


def input_array():
    num_array = list()
    num = input("Enter how many elements you want:")
    print('Enter numbers in array: ')
    for i in range(int(num)):
        n = input("num :")
        num_array.append(int(n))
    return num_array


@TraceCalls()
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
    # print('With v')
    # res = count_values(power, *arr, step=3)
    # print(res)
    # print('Without v')
    # res = count_values(power, *arr, step=3, as_list=True)
    # print(res)
    # print('Match')
    match(*arr, simple=True)


if __name__ == "__main__":
    main()
