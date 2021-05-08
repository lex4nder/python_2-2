class SchoolBoy:
    def __init__(self, name, homework: list):
        self.name = name
        self.__homework = homework

    def show_homework(self, subj):
        if self.__homework_done(subj):
            return 'here it is.'
        else:
            return 'haven\'t done it.'

    def __homework_done(self, subj):
        if subj in self.__homework:
            return True
        return False


ben = SchoolBoy('Ben', ['maths', 'english'])
print('maths:', ben.show_homework('maths'))
print('biology:', ben.show_homework('biology'))
