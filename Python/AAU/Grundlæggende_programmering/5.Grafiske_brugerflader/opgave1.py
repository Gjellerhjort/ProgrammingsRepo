import math

f = lambda x: x**2-1

g = lambda x,y: math.sqrt(x**2+y**2)

h = lambda x: 0 if x <= 0 else x

f_test = [-1, 0, 1]
g_test = [(1, 1), (3, 4), (6, 8)]
h_test = [-1, 0, 1]

f_result = [f(x) for x in f_test]
g_result = [g(x,y) for x,y in g_test]
h_result = [h(x) for x in h_test]


print("f(x) tests:", f_result)
print("g(x, y) tests:", g_result)
print("h(x) tests:", h_result)