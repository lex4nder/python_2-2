inp = input()
bl = True

for i in range(len(inp) // 2):
    if inp[i] == inp[-i - 1]:
        pass
    else:
        print('is not a palindrome.')
        bl = False
        break
if bl:
    print('is a palindrome.')
