import time

inp = input('Enter your birth date (DD.MM.YYYY): ')
bday = time.mktime(time.strptime(inp, '%d.%m.%Y'))
secs_alive = time.time() - bday
print(f'You\'ve been alive for {"{:.1f}".format(secs_alive / (3600 * 24))} days.')
