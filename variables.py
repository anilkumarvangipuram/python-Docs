a=10
def f1():
    a=777
    print(globals()['a'])
f1()