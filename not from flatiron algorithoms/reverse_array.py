def reverse_array(arr):
    return arr[::-1]   




if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(f'input: {arr}')
    print('expected output: [4, 3, 2, 1]')
    print(f'result: {reverse_array(arr)}')