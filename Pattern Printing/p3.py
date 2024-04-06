class Solution:
    def printPattern(self, n):
        for row in range(1, 2*n):
            if row > n:
                tcol = 2*n-1-row+1
            else:
                tcol = row
            for col in range(1, tcol+1):
                print('*', end = " ")
            print()
            
if __name__ == "__main__":
    num_rows = 5

    ob = Solution()

    ob.printPattern(num_rows)