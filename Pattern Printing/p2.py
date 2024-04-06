class Solution:
    def printPattern(self, n):
        for row in range(1, n+1):
            for col in range(1, n+1):
                print("*", end = " ")
            print()

if __name__ == "__main__":
    n = 4

    ob = Solution()

    ob.printPattern(n)