
class Solution:
    def left_rotation(self, d, arr):
        # simply removes the 1st item and appends it at the end
        for _ in range(d):
            removed = arr.pop(0)
            arr.append(removed)
        return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    x = "expecting =>"

    s = Solution()
    print("expecting => [2, 3, 4, 5, 1]")
    print("result    =>",(s.left_rotation(1, arr)))
    print()
    print("expecting => [4, 5, 1, 2, 3]")
    print("result    =>",(s.left_rotation(22, arr)))