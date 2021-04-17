class Triangle:
    def __init__(self, color):
        self.color = color


class Rectangle:
    def __init__(self, color):
        self.color = color


class Circle:
    def __init__(self, color):
        self.color = color


class Box:
    def __init__(self):
        self.triangles = []
        self.rectangles = []
        self.circles = []

    def print_info(self):
        print(f'There are: {len(self.circles)} circle(s) ({", ".join([circle.color for circle in self.circles])}), '
              f'{len(self.rectangles)} rectangle(s) ({", ".join([rectangle.color for rectangle in self.rectangles])}), '
              f'{len(self.triangles)} triangle(s) ({", ".join([triangle.color for triangle in self.triangles])}).')

    def add_figure(self, figure):
        if isinstance(figure, Triangle):
            self.triangles.append(figure)
        elif isinstance(figure, Rectangle):
            self.rectangles.append(figure)
        elif isinstance(figure, Circle):
            self.circles.append(figure)


t1 = Triangle('black')
t2 = Triangle('blue')
t3 = Triangle('green')
c1 = Circle('yellow')
c2 = Circle('teal')
r1 = Rectangle('pink')
box = Box()

box.add_figure(t1)
box.add_figure(t2)
box.add_figure(t3)
box.add_figure(c1)
box.add_figure(c2)
box.add_figure(r1)
box.print_info()
