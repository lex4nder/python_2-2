inp = list(input())
inp_st = set(inp)
if len(inp) == len(inp_st):
    print('No duplicates in this line.')
else:
    print(f'There are some duplicating characters in this line.')
