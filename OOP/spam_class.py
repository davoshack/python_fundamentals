# File spam_class.py

class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances(cls):
        print('Number of instances: %s %s' % (cls.numInstances, cls))

    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):
        print('Extra stuff...', cls)
        Spam.printNumInstances()

    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass

