from random import randint

class Solution:
    def hourglass_sum(self, grid):

        for i in range(len(grid)):
            print(grid[i])

        all_hourglass_sums = []

        
        for i in range    ( 1, len(grid) -1  ):
            for j in range( 1, len(grid) - 1 ):
                all_hourglass_sums.append(sum([ grid[i-1][j-1], 
                                                grid[i-1][j],
                                                grid[i-1][j+1],
                                                    
                                                grid[i][j],
                                               
                                                grid[i+1][j-1],
                                                grid[i+1][j],
                                                grid[i+1][j+1]                                                                                          
                                               ])),
        print()        
        print("amount of hourglasses =>", len(all_hourglass_sums))
        print()
        # for each in all_hourglass_sums:
        #     print(each)

        highest_sum = all_hourglass_sums[0]
        for each in all_hourglass_sums:
            if each > highest_sum:
                highest_sum = each
        return str("highes sum hourglass: " + str(highest_sum))
            
        


if __name__ == '__main__':
    # creates the 2D array, aka: "grid"
    grid = []
    for x in range(6):
        row = []
        for x in range(6):
            row.append(randint(-9, 9))
        grid.append(row)

    s = Solution()
    print(s.hourglass_sum(grid))   