import copy

a = [11, 22]

b = a

print(id(a))

print(id(b))

c = copy.copy(a)

print(id(c))