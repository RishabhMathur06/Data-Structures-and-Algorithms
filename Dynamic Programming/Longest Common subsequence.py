'''
    Name: Rishabh Mathur
    Date: 16 Mar, 2024
'''

class Solution:
    def lcs(self,x,y,s1,s2):
        # code here
        dp = [ [None]*(y+1) for i in range(x+1) ]
        
        for i in range(x+1):
            for j in range(y+1):
                if(i==0 or j==0):
                    dp[i][j] = 0
                    
                elif(s1[i-1] == s2[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[x][y]

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
