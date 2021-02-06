seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}


def what_season(n):
    try:
        if int(n) in range(1, 13):
            for i in range(4):
                if int(n) in seasons[list(seasons.keys())[i]]:
                    return f'This month is in {list(seasons.keys())[i]}.'
                else:
                    pass
        else:
            return 'Not a number of a month.'
    except ValueError:
        return 'Please enter a number.'


inp = input()
print(what_season(inp))
