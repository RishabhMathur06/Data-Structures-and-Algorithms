'''
    Name: Rishabh Mathur
    Date: 4 May, 2024
'''

class Solution:
    def arraySortedOrNot(self, arr, n):
        ans = 1
        
        for i in range(n-1):
            if(arr[i+1] < arr[i]):
                ans = 0
                
        return ans

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1
