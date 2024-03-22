'''
    Name: Rishabh Mathur
    Date: 22 Mar, 2024
'''

class Solution:
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[False]*(n+1) for i in range(m+1)]
         
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                     dp[i][j] = 0
                     
                elif(X[i-1] == Y[j-1]):
                     dp[i][j] = 1+dp[i-1][j-1]
                     
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        lcs = dp[m][n]
        
        res = m+n-lcs
        
        return res

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        