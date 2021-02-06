import sys

inp = list(input('Enter a number: '))
for i in range(len(inp)):
    try:
        inp[i] = int(inp[i])
    except ValueError:
        print('Please enter a number without any other characters.')
        sys.exit()
print(sum(inp))
