'''
    Name: Rishabh Mathur
    Date: 28 Feb, 2024
'''

class Solution:
    def subsetSum(self, arr, sum):
        # Building dp table
        dp = [[False for j in range(sum+1)] for i in range(len(arr)+1)]
        
        # Initializing DP
        for i in range(len(arr)+1):
            for j in range(sum+1):
                if(i == 0):
                    dp[i][j] = False
                    
                if(j == 0):
                    dp[i][j] = True
                    
        # filling rest of the dp
        for i in range(1, len(arr)+1):
            for j in range(1, sum+1):
                if(arr[i-1] <= j):
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                
        return dp[len(arr)][sum]
    
    def equalPartition(self, N, arr):
        # code here
        sum = 0
        
        for i in range(N):
            sum += arr[i]
            
        if (sum % 2 != 0):
            return 0
            
        else:
            return self.subsetSum(arr, sum//2)

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
