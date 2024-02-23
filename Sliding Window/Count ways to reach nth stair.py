'''
    Name: Rishabh Mathur
    Date: 23rd feb, 2024
'''

mod = 1e9 + 7

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # code here
        prev_2 = 1
        prev = 1
        
        for i in range(2, n+1):
            curr = int((prev%mod + prev_2%mod)%mod)
            
            prev_2 = prev
            prev = curr
            
        return prev

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
