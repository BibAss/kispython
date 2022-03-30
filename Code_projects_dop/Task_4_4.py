class Num:
    result = "0"
    value = 0
    stack = "0"

    def __init__(self, v):
        self.result = str(v)
        self.value = v
        self.stack = "PUSH " + str(v)


class Add:
    result = "0"
    value = 0
    stack = ""

    def __init__(self, a, b):
        self.result = "(" + str(a.result) + " + " + str(b.result) + ")"
        self.value = a.value + b.value
        self.stack = a.stack + '\n' + b.stack + '\n' + "ADD"


class Mul:
    result = "0"
    value = 0
    stack = ""

    def __init__(self, a, b):
        self.result = "(" + str(a.result) + " * " + str(b.result) + ")"
        self.value = a.value * b.value
        self.stack = a.stack + '\n' + b.stack + '\n' + "MUL"


class PrintVisitor:

    def __init__(self):
        pass

    def visit(self, a):
        return a.result


class CalcVisitor:
    def __init__(self):
        pass

    def visit(self, a):
        return a.value


class StackVisitor:
    code = "0"

    def __init__(self):
        pass

    def visit(self, a):
        self.code = a.stack

    def get_code(self):
        return self.code


ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())
