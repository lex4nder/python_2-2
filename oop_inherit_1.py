class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.length, self.width, self.height)


class Kitchen(Table):

    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.places = None

    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplaces(self):
        print(self.places)


class Desk(Table):
    def __init__(self, l, w, h):
        super().__init__(l, w, h)

    def is_for_children(self):
        if self.height < 70:
            return True
        return False

    def outplaces(self):
        print(self.length, self.width, self.height, f'For children: {self.is_for_children()}')


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplaces()
t_2 = Table(1, 3, 0.7)
t_2.outing()

desk_1 = Desk(120, 60, 75)
desk_2 = Desk(100, 60, 65)
desk_1.outplaces()
desk_2.outplaces()
