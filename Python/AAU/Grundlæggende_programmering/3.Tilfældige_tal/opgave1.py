import random
import numpy as np

# opgave 1
print("-"*10+"Opgave 1" + "-"*10)
n1 = [random.randint(0,1) for i in range(10)]
print(n1)
# opgave 2
print("-"*10+"Opgave 2" + "-"*10)
n2 = [random.randint(6,10) for i in range(10)]
print(n2)
# opgave 3
print("-"*10+"Opgave 3" + "-"*10)
n3 = np.random.normal(0, 1, 10)
print(n3)
# opgave 4
print("-"*10+"Opgave 4" + "-"*10)
#n4 = np.random.normal(0, -3, 4)
#print(n4)

# opgave 5
print("-"*10+"Opgave 5" + "-"*10)
n5 = [random.randrange(0,2) for i in range(10)]
print(n5)
# opgave 6
print("-"*10+"Opgave 6" + "-"*10)
random.seed(10)
n6 = [random.randrange(0,2) for i in range(10)]
print(n6)
random.seed(10)
n6 = [random.randrange(0,2) for i in range(10)]
print(n6)
# opgave 7
print("-"*10+"Opgave 7" + "-"*10)
n7_list = ['Tic','Tac','Toe']
n7 = [random.choice(n7_list) for i in range (10)]
print(n7)