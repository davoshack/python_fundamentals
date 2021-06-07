# File private0.py


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


if __name__ == '__main__':
    x = Test1()
    y = Test2()

    # Works
    x.name = 'Bob'

    # Fails
    y.name = 'Sue'
    print(x.name)

    # Works
    y.age = 30

    # Fails
    x.age = 40
    print(y.age)
