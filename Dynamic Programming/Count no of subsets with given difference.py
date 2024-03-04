'''
    Name: Rishabh Mathur
    Date: 4 Mar, 2024
'''

MOD = 10**9+7

class Solution:
    def countSubsets(self, arr, n, sum1):
        dp = [[0 for j in range(sum1+1)] for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(sum1+1):
                if(i == 0):
                    dp[i][j] = 0
                    
                if(j == 0):
                    dp[i][j] = 1
                    
        for i in range(1, n+1):
            for j in range(sum1+1):
                if(arr[i-1] <= j):
                    dp[i][j] = (dp[i-1][j - arr[i-1]] + dp[i-1][j])%MOD
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][sum1] 
                
    def countPartitions(self, n, d, arr):
        tot = sum(arr)
        
        if((tot+d) % 2 != 0 or (tot+d)<0):
            return 0
            
        sum1 = (d+tot)//2
        
        return self.countSubsets(arr, n, sum1)

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, d = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countPartitions(n, d, arr)
        print(res)
