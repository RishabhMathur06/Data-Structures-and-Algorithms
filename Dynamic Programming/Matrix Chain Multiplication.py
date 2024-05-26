'''
    Name: Rishabh MAthur
    Date: 26 May
'''
class Solution:
    def solve(self, arr, i, j, dp):
        if( i >= j):
            return 0
            
        if(dp[i][j] != -1):
            return dp[i][j]
            
        mn = float("inf")
            
        for k in range(i, j):
            temp = self.solve(arr, i, k, dp) + self.solve(arr, k+1, j, dp) + (arr[i-1]*arr[k]*arr[j])
            
            mn = min(temp, mn)
            
        dp[i][j] = mn
                
        return dp[i][j]
    
    def matrixMultiplication(self, N, arr):
        # code here
        dp = [[-1]*(N+1) for i in range(N+1)]
        
        return self.solve(arr, 1, N-1, dp)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
