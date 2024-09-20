# create a rectangle with side lengths a, b
sides = (3,4)
a, b = sides 

def rectangle_info(a,b):
    global circumference
    area = a*b
    circumference = 2*a+ 2*b
    return(area, circumference)

area, circumference = rectangle_info(*sides)

print(f'A rectangle with sidelengths {a} and {b} has area {area} and circumference {circumference}')