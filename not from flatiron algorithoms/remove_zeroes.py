array     = [9, 0, 0, 6, 0, 3, 0, 5]
# result  = [3, 0, 0, 5, 0, 6, 0, 9]

class Solution:
    def remove_zeroes(self, array):

        final_list = []

        temp = []
        for num in array:
            temp.append(num) if num != 0 else None 
        no_zeroes = sorted(temp)
        
        for i, v in enumerate(array):
            if v == 0:
                final_list.append(array[i])
            else:
                final_list.append(no_zeroes[0])
                del no_zeroes[0]

        return (final_list) 
        







if __name__ == '__main__':
    s = Solution()
    print((s.remove_zeroes(array)))