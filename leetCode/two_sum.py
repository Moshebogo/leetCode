class Solution(object):
    def twoSum(self, nums, target):

        for indexI, valueI in enumerate(nums):
               print("indexI =>", indexI, "valueI =>", valueI)
               for indexJ, valueJ in enumerate(nums, indexI+1):
                   print("indexJ =>", indexJ, "valueJ =>", valueJ)

if __name__ == '__main__':     
    s = Solution()
    print(list(s.twoSum([1, 2, 3, 4], 6)))