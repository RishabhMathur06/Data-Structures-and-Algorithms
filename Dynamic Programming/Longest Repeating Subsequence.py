'''
    Name: Rishabh Mathur
    Date: 30 Mar, 2024
'''

class Solution:
    def LongestRepeatingSubsequence(self, str):
        a = str
        b = str
        
        n = len(str)
        m = len(str)
        
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif a[i-1] == b[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[n][m]

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.LongestRepeatingSubsequence(str)
        print(ans)
