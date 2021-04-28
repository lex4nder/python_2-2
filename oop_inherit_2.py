class Figure:
    def __init__(self):
        self.color = 'white'

    def change_color(self, color):
        self.color = color

    def info(self):
        pass


class Oval(Figure):
    def __init__(self, r1, r2):
        super().__init__()
        self.r1 = r1
        self.r2 = r2

    def info(self):
        print('Oval', self.color, self.r1, self.r2)


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def info(self):
        print('Square', self.color, self.a)


o1 = Oval(20, 18)
s1 = Square(5)
s2 = Square(50)
s2.change_color('red')
o1.info()
s1.info()
s2.info()
