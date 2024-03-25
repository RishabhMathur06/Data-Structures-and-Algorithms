'''
    Name: Rishabh Mathur
    Date: 25 Mar, 2024
'''

class Solution:
    def minimumNumberOfDeletions(self,S):
        s1 = S
        s2 = S[::-1]
        
        n = len(s1)
        m = len(s2)
        
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if(i==0 or j==0):
                    dp[i][j] = 0
                    
                elif(s1[i-1] == s2[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        lcs = dp[n][m]
        
        return n-lcs

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
