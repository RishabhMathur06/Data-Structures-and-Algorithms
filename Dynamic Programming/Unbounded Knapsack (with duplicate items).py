'''
    Name: Rishabh Mathur
    Date: 7 Mar, 2024
'''

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp = [[0 for j in range(W+1)] for i in range(N+1)]
        
        for i in range(N+1):
            for j in range(W+1):
                if(wt[i-1] <= j):
                    dp[i][j] = max(val[i-1]+dp[i][j - wt[i-1]], dp[i-1][j])
                    
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[N][W]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
