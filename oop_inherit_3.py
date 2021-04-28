class Architect:
    def __init__(self, name):
        self.name = name
        self.projects = []
        self.coworkers = []

    def new_coworker(self, coworker):
        self.coworkers.append(coworker)

    def new_project(self, project):
        self.projects.append(project)

    def info(self):
        print(self.name, self.projects, [coworker.name for coworker in self.coworkers])


class MainArchitect(Architect):
    def __init__(self, name):
        super().__init__(name)
        self.subordinates = []

    def new_project(self, project):
        if len(self.subordinates) >= 2:  # для простоты будем считать, что для стандартного проекта нужно два подчинённых
            pass
        elif self.get_subordinates(2):
            self.get_subordinates(2)
        else:
            print('There are not enough people to take part in the project.')
            return False
        self.projects.append(project)
        self.assign_to_subordinates(project)

    def assign_to_subordinates(self, project):
        self.subordinates[0].new_coworker(self.subordinates[1])
        self.subordinates[1].new_coworker(self.subordinates[0])
        for i in range(2):
            self.subordinates[0].new_project(project)
            self.subordinates.remove(self.subordinates[0])

    def get_subordinates(self, n):
        global free_workers
        if len(free_workers) >= n:
            for i in range(n):
                self.subordinates.append(free_workers.pop(0))
            return True
        else:
            return False

    def info(self):
        print(self.name, [coworker.name for coworker in self.coworkers],
              self.projects, [subordinate.name for subordinate in self.subordinates])


dan = Architect('Dan')
john = Architect('John')
layla = Architect('Layla')
carrie = Architect('Carrie')
free_workers = [dan, john]


sergio = MainArchitect('Sergio')

sergio.new_project('SkyCity')
print(free_workers)
sergio.new_project('School n98')
print()

free_workers.append(layla)
free_workers.append(carrie)

sergio.new_project('School n98')

sergio.info()
john.info()
dan.info()
layla.info()
carrie.info()
