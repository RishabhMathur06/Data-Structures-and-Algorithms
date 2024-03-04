'''
    Name: Rishabh Mathur
    Date: 4 Mar, 2024
'''

mod = 10**9+7
class Solution:
    def countSubsets(self, arr, n, sum):
        dp = [[0 for j in range(sum+1)] for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(sum+1):
                if(i == 0):
                    dp[i][j] = 0
                    
                if(j == 0):
                    dp[i][j] = 1
                            
        for i in range(1, n+1):
            for j in range(sum+1):
                if(arr[i-1] <= j):
                    dp[i][j] = (dp[i-1][j - arr[i-1]] + dp[i-1][j])%mod
                    
                else:
                    dp[i][j] = (dp[i-1][j])%mod
                    
        return dp[n][sum]
        
    def findTargetSumWays(self, n, arr, target):
        # code here 
        target = abs(target)
        
        for i in range(n):
            arr[i] = abs(arr[i])
            
        s1 = sum(arr)
        
        # If sum of all elements and target is odd, no splits possible to acheive the "target"
        if( ((s1+target)%2 != 0)):
            return 0
            
        s1 = (s1+target)//2
        
        return self.countSubsets(arr, n, s1)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(N, arr, target))
