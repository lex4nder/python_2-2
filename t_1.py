import time

while True:
    try:
        inp = float(input('Enter a number: '))
        if inp >= 0:
            time.sleep(inp)
        else:
            break
    except ValueError:
        inp = float(input('Enter a number without any other characters: '))
