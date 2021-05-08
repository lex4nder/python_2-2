class Guitar:
    def __init__(self, string_n, tuning):
        self.__string_n = string_n
        self.__tuning = tuning

    def change_tuning(self, new_tuning):
        tuning = list(new_tuning.lower())
        if len(tuning) != self.__string_n:
            return 'There are more strings'
        for s in tuning:
            if s not in list('abcdefg'):
                return f'There is no {s} note'
        self.__tuning = new_tuning
        return self.__tuning

    def remove_string(self):
        if self.__string_n > 0:
            self.__string_n -= 1
            return self.__string_n
        return 'This guitar already has no strings'


guitar = Guitar(6, 'EBGDAE')
print(guitar.change_tuning('EBGDB'))
print(guitar.change_tuning('EBGDAH'))
print(guitar.change_tuning('EBGDAD'))

print(guitar.remove_string())
for i in range(5):
    guitar.remove_string()
print(guitar.remove_string())
