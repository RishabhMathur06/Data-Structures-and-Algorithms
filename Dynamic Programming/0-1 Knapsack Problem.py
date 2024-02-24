'''
    Name: Rishabh Mathur
    Date: 24 Feb, 2024
'''

class Solution:
    def knapsackUtil(self, W, wt, val, n, t):
        if(n == 0 or W == 0):
            return 0
            
        if(t[n][W] != -1):
            return t[n][W]
            
        if(wt[n-1] <= W):
            t[n][W] = max(val[n-1]+self.knapsackUtil(W-wt[n-1], wt, val, n-1, t), self.knapsackUtil(W, wt, val, n-1, t))
            return t[n][W]
            
        elif(wt[n-1] > W):
            t[n][W] = self.knapsackUtil(W, wt, val, n-1, t)
            return t[n][W]

    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        t = [[-1 for i in range(W+1)] for j in range(n+1)]
        # code here
        ans = 0
        
        ans = self.knapsackUtil(W, wt, val, n, t)
        
        return ans

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
