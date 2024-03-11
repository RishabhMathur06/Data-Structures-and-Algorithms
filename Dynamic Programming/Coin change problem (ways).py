'''
    Name: Rishabh Mathur
    Date: 11 Mar, 2024
'''

class Solution:
    def count(self, coins, N, sum):
        dp = [[0] * (sum + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            dp[i][0] = 1
        
        for i in range(1, N + 1):
            for j in range(sum + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                    
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[N][sum]

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))
