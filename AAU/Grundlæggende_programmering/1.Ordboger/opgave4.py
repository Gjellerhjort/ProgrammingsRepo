
def square(n: int) -> dict:
    result = {}
    for n in range(0, n+1):
        result[n] = n ** 2
    return result

print(square(5))