# File spam_static_deco.py

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print('Number of Instances created: %s' % Spam.numInstances)

