'''
    date: 2 Mar, 2024
    Name: Rishabh Mathur
'''
class Solution:
    def countSubsets (self, N, arr, sum):
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
                    t[i][j] = t[i-1][j - int(arr[i-1])] + t[i-1][j]
                    
                else:
                    t[i][j] = t[i-1][j]
                    
        return t[n][W]

if __name__ == '__main__': 
    ob = Solution()

    arr = [2, 3, 5, 6, 8, 10]
    sum  = 10
    N = len(arr)

    print(ob.countSubsets(N, arr, sum))
