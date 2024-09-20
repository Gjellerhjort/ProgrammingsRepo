def divide(a, b) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return 0
    


result = divide(4,2)
print(result)
result = divide(4,0)
print(result)