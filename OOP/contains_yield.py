# File contains_yield.py
# 2.X/3.X compatibility
from __future__ import print_function

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> next', end='')
        for x in self.data:
            yield x
            print('next:', end='')

    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data


if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end='  |  ')

    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))

    Itr = iter(X)
    while True:
        try:
            print(next(Itr), end='  @  ')
        except StopIteration:
            break
