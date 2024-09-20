p2 = {10: 2, 0: -48}

def polynomial(x: int, p: dict) -> int:
    result: int = 0
    for i in p:
        if i == 0:
            result = result+p[i]
        else:
            result = result+p[i]*x**i
        
    return result


polynomial(2, p2)