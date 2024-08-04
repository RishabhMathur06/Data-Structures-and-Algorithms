'''
    Name: Rishabh Mathur
    Date: 4 Aug, 2024
'''

class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        
        i, j = 0, 0
        summ = 0
        minm = float("inf")
        
        while j < n:
            while summ <= x and j < n:
                summ += arr[j]
                j += 1
            
            while summ > x and i < n:
                minm = min(minm, j - i)
                summ -= arr[i]
                i += 1
        
        if minm == float("inf"):
            return 0
        else:
            return minm

def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1

if __name__ == "__main__":
    main()