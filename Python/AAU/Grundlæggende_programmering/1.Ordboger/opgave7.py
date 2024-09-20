

def divide(a, b=1) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        return 0
    