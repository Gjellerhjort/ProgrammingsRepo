from matrix import Matrix

a = Matrix([
    [1,3],
    [3,4]
])

b = Matrix([
    [8,3],
    [2,3]
])

c = Matrix([
    [8]
])
print(a)
print("-- * --")
print(b)
print("-- = --")
d = c.determinant()
print(d)
