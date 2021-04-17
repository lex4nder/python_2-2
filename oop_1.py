class Shop:
    def __init__(self):
        self.visitors_total = 0

    def print_info(self):
        print(f'There\'s been {self.visitors_total} visitor(s) total.')


class Person:
    def __init__(self):
        self.shops_visited = 0

    def visit_shop(self, shop: Shop):
        shop.visitors_total += 1
        self.shops_visited += 1


a_guy = Person()
another_guy = Person()
a_shop = Shop()

a_guy.visit_shop(a_shop)
another_guy.visit_shop(a_shop)
a_shop.print_info()
