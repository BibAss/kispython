class Automate:
    state = ""

    def __init__(self, x):
        self.state = x

    def load(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "B":
            self.state = "C"
            return 1
        elif self.state == "E":
            self.state = "A"
            return 6
        elif self.state == "F":
            self.state = "A"
            return 8
        else:
            raise KeyError()

    def code(self):
        if self.state == "C":
            self.state = "D"
            return 3
        elif self.state == "E":
            return 7
        else:
            raise KeyError()

    def shade(self):
        if self.state == "D":
            self.state = "E"
            return 4
        elif self.state == "B":
            self.state = "E"
            return 2
        elif self.state == "E":
            self.state = "F"
            return 5
        else:
            raise KeyError("KeyError")


def main():
    return Automate("A")


o = main()
o.load()  # 0
o.code()  # KeyError
o.shade()  # 2
o.load()  # 6
o.load()  # 0
o.load()  # 1
o.code()  # 3
o.shade()  # 4
o.code()  # 7
o.shade()  # 5
o.load()  # 8
o.load()  # 0
