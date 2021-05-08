class Notebook:
    def __init__(self, sheets_n, cover):
        self.sheets_n = sheets_n
        self._cover = cover
        self.__type = 'notebook'


notebook = Notebook(24, 'hard')
print(notebook.sheets_n, notebook._cover)
print(notebook.__type)
