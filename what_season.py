seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}


def what_season(n):
    try:
        n = int(n)
    except ValueError:
        return 'Please enter a number.'
    for season_name, month_ids in seasons.items():
        if n in month_ids:
            return f'It\'s {season_name}'
        else:
            return 'It\'s not a number of a month.'


inp = input()
print(what_season(inp))
