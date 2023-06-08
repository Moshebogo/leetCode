
# some recursion some
def test(num):
    if num == 0:
        return
    print(num)
    return test(num-1)


print(test(10))