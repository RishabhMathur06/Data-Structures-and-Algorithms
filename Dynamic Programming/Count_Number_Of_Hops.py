#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        modulo = 10**9 + 7
        # code here                 #  0  1  2  3  4
        count = [0] * (n+1) # count = [0, 0, 0, 0, 0]
        
        count[0] = 1
        
        if(n >= 1):
            count[1] = 1
            
        if(n >= 2):
            count[2] = 2            # [1, 1, 2, 0, 0]
            
        for i in range(3, n+1):
            count[i] = (count[i-1] + count[i-2] + count[i-3]) % modulo # [1 1 2 4 0]
                                                             # [1 1 2 4 7]
        return count[n]
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends
