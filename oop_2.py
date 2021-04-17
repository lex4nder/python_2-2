class Phone:
    def __init__(self, brand, os, color):
        self.brand = brand
        self.os = os
        self.color = color

    def print_info(self):
        print(f'it\'s a {self.color} {self.brand} powered by {self.os}')


phone_1 = Phone('Iphone', 'IOS', 'black')
phone_2 = Phone('Huawei', 'Android', 'blue')
phone_3 = Phone('Nokia', 'WP', 'yellow')

phone_1.print_info()
phone_2.print_info()
phone_3.print_info()
