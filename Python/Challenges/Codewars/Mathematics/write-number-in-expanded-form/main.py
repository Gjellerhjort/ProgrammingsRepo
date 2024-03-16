
def expanded_form(num):
    num_str = str(num)
    i = len(num_str)-1
    expanded_list = []
    for digit in num_str:
        if digit != '0':
            expanded_string = digit + i*'0'
            expanded_list.append(expanded_string)
        i=i-1

    result = " + ".join(expanded_list)
    print(result)

def sample_tests():
    def test(result, answer):
        if result == answer:
            print("pass")

    test(expanded_form(12), '10 + 2');
    test(expanded_form(42), '40 + 2');
    test(expanded_form(70304), '70000 + 300 + 4');


sample_tests()