import os


def add(a, b):
    c = a + b
    return c


def intersect(set1, set2):
    c = set1 & set2
    return c


def extend_line(a, b):
    c = a + b
    return c


def change_common_elements(a, b):
    for i in range(len(a)):
        if a[i] in b:
            a[i] = 0


def new_folder_w_f(path):
    os.makedirs(path, exist_ok=True)
    with open(f'{path}test.txt', 'w') as f:
        f.write('some stuff')
