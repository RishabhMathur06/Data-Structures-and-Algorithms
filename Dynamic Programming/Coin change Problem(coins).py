'''
    Name: Rishabh Mathur
    Date: 14 Mar, 2024
'''

class Solution:
    def minCoins(self, coins, M, Sum):
        # code here
        dp = [[0]*(Sum+1) for i in range(M+1)]

        for i in range(M+1):
            for j in range(Sum+1):
                if i == 0:
                    dp[i][j] = float("inf")-1
                    
                if j == 0:
                    dp[i][j] = 0

        for i in range(1, 2):
            for j in range(1, Sum+1):
                if j % coins[0] == 0:
                    dp[i][j] = j // coins[0]
                else:
                    dp[i][j] = float("inf")-1
                    
        for i in range(2, M+1):
            for j in range(1, Sum+1):
                if coins[i-1] <= j:
                    dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        if dp[M][Sum] == float("inf")-1:
            return -1
        else:
            return dp[M][Sum]

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        v,m = input().split()
        v,m = int(v), int(m)
        coins = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCoins(coins,m,v)
        print(ans)
