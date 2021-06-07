# File specialize.py
"""
Defines multiple classes that illustrate a variety
of common techniques:
    super
        Defines a method function and a delegate that
        expects an action in a subclass.
    Inheritor
        Doesn't provide any new names, so it gets everything
        defined in Super.
    Replacer
        Overrides Super's method with a version of its own.
    Extender
        Customizes Super's method by overriding and calling
        back to run the default.
    Provider
        Implements the action method expected by Super's delegate method.
"""


class Super:
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

    print('\nProvider...')
    x = Provider()
    x.delegate()
