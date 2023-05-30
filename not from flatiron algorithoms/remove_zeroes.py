heights   = [9, 0, 0, 6, 0, 3, 0, 5]
# result  = [3, 0, 0, 5, 0, 6, 0, 9]

def indexed(array_2):
   array = array_2
   indexed = []
   for num in array:
       if num == 0:
           indexed.append(array.index(num))
           array.pop(num)
           print("array =>", array)
   return indexed       


class Solution:
    def remove_zeroes(self, array):
       pass
        



if __name__ == '__main__':
    s = Solution()
    # print(s.remove_zeroes(heights))
    print(indexed(heights))

