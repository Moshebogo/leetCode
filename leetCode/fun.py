
# some recursion some
def test(num):
    if num == -995:
        return  None
    print(num)
    return test(num-1)


print(test(0))