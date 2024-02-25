'''
    Name: Rishabh Mathur
    Date: 25 Feb, 2024
'''

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        n = len(arr)
        W = sum
        
        t = [[False for j in range(W+1)] for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(W+1):
                if(i==0):
                    t[i][j] = False
                    
                if(j == 0):
                    t[i][j] = True
                    
        for i in range(1, n+1):
            for j in range(1, W+1):
                
                if(int(arr[i-1]) <= j):
                    t[i][j] = t[i-1][j - int(arr[i-1])] or t[i-1][j]
                    
                else:
                    t[i][j] = t[i-1][j]
                    
        return t[n][W]

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
