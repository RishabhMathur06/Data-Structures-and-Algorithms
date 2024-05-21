''' 
    Name: Rishabh Mathur
    Date: 21st May, 2024
'''
MOD = 10**9+7

class Solution:
    def Maximize(self, a, n): 
        arr.sort()
        res = 0
        
        for i in range(n):
            res += arr[i]*i
        
        ans = res % MOD
        return ans

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))