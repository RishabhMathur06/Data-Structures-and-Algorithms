'''
    Name: Rishabh Mathur
    Date: 2 Apr, 2024
'''

class Solution:
    def isSubSequence(self, A, B):
        n = len(A)
        m = len(B)
        
        dp = [[0]*(m+1) for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if (i==0 or j==0):
                    dp[i][j] = 0
                    
                elif (A[i-1] == B[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                    
        lcs = dp[n][m]
        
        if(lcs == n):
            return True
            
        return False

if __name__ == "__main__":
    ob = Solution()

    A = "AXY"
    B = "ADXCPY"

    print(ob.isSubSequence(A, B))