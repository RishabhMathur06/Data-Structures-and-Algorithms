'''
    Name: Rishabh Mathur
    Date: 22 Mar, 2024
'''
class Solution:
    def LCS(self, dp, s1, s2, n, m):
        for i in range(n+1):
            for j in range(m+1):
                if(i == 0 or j == 0):
                    dp[i][j] = 0

                elif(s1[i-1] == s2[j - 1]):
                    dp[i][j] = 1+dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    def printLCS(self, s1, s2, n , m):
        dp  = [[False]*(m+1) for i in range(n+1)]

        self.LCS(dp, s1, s2, n, m)

        res = ""
        i = n
        j = m

        while(i > 0 and j > 0):
            if(s1[i-1] == s2[j-1]):
                res += (s1[i-1])
                i -= 1
                j -= 1

            else:
                if(dp[i][j-1] > dp[i-1][j]):
                    j -= 1

                else:
                    i -= 1
        
        return res[::-1]

if __name__ == "__main__":
    s1 = "acbcf"
    s2 = "abcdaf"

    n = len(s1)
    m = len(s2)

    ob = Solution()

    print("First string: acbcf")
    print("Second String: abcdaf")
    print("\nThe longest common subsequence is: ")
    print(ob.printLCS(s1, s2, n, m))