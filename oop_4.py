import random


class Ticket:
    def __init__(self, num, train):
        self.num = num
        self.train = train


class Person:
    def __init__(self):
        self.tickets = []

    def get_ticket(self, train, office):
        ticket = random.choice(office.tickets_available(train))
        office.sell_ticket(ticket, self)

    def print_info(self):
        print(f'The man has the following tickets: {[ticket.num for ticket in self.tickets]}')


class TicketOffice:
    def __init__(self, ticket_list):
        self.tickets = ticket_list

    def tickets_available(self, train):
        ts = []
        for ticket in self.tickets:
            if ticket.train == train:
                ts.append(ticket)
        return ts

    def sell_ticket(self, ticket, person):
        self.tickets.remove(ticket)
        person.tickets.append(ticket)

    def print_info(self):
        print(f'The office has the following tickets: {[ticket.num for ticket in self.tickets]}')


t11 = Ticket(1, '1')
t21 = Ticket(2, '1')
t31 = Ticket(3, '1')
t42 = Ticket(4, '2')
man = Person()
t_office = TicketOffice([t11, t21, t31, t42])
man.get_ticket('1', t_office)

man.print_info()
t_office.print_info()
