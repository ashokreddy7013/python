def sample():
    no= 1
    print(no)
    no+=1
    yield no

    print(no)
    no += 1
    yield no

a = sample()
print(next(a))
print(next(a))
print(next(a))