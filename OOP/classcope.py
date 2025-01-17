# File classcope.py

X = 1


def nester():
    print(X)                # Global: 1

    class C:
        print(X)            # Global: 1

        def method1(self):
            print(X)        # Global: 1

        def method2(self):
            X = 3           # Hide Global
            print(X)        # Local: 3

    I = C()
    I.method1()
    I.method2()


print(X)                    # Global: 1
nester()                    # Rest: 1, 1, 1, 3
print('-'*40)
