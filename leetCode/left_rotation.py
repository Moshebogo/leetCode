
class Solution:
    def left_rotation(self, d, arr):
        # simply removes the 1st item and inserts it at the end
        def actually_rotate(array):
                removed = array.pop(0)
                array.insert(-1, removed)
                return array
        # perform 'actually_rotate' however many times 'd' is 
        for _ in range(d):
            x = actually_rotate(array)
        return x                       

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]

    s = Solution()
    print((s.left_rotation(array, 54)))