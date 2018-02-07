

class Root:
    def __init__(self):
        print("this is root")

class A1(Root):
    def __init__(self):
        super(A1, self).__init__()
        print("this is A1")

class A2(Root):
    def __init__(self):
        super(A2, self).__init__()
        print("this is A2")


class B(A1, A2):
    def __init__(self):
        super(B, self).__init__()
        print("this is B")

if __name__ == '__main__':
    a1 = A1()
    a2 = A2()
    b = B()
    print("=========")
    c1 = a1.__class__.mro()
    c2 = a2.__class__.mro()
    b = b.__class__.mro()
    print(c1)
    print(c2)
    print("B", b)
