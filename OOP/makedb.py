# File makedb.py: store Person objects on a shelve database

from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=1000000)
tom = Manager('Tom Jones', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

