class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(len(nums)):
            temp = nums[x]
            print(temp)
            for x in range(1, len(nums)):
                if nums[x] + temp == target:
                    print(nums[x])
                    return [nums.index(temp), nums.index(nums[x])]


        



if __name__ == '__main__':     
    s =Solution()
    print(list(s.twoSum([3, 3], 6)))