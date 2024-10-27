function_str = """
def f(x):
    if x >= 0:
        return x
    else:
        return 0
"""

exec(function_str)

# Test funktionen med værdierne x = -1, 0, og 1
test_values = [-1, 0, 1]
results = {x: f(x) for x in test_values}

print(results)