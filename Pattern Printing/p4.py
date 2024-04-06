class Solution:
    def printPattern(self, n):
        for row in range(1, n+1):
            for col in range(1, n+1-row):
                print(" ", end=" ")
            for col in range(1, row+1):
                print("*", end=" ")
            print()
            
if __name__ == "__main__":
    num_rows = 5

    ob = Solution()

    ob.printPattern(num_rows)