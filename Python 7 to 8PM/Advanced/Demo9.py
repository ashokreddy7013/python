
def sum():
    no = 0
    no += 1
    yield no

    no += 1
    yield no

    no += 1
    yield no

i = sum()
print(next(i))
print(next(i))
print(next(i))
print(next(i))