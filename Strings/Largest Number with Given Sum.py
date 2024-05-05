'''
    Name: Rishabh Mathur
    Date: 5 May,2024
'''

class Solution:
    def largestNum(self,n,sum):
        res = ""
        
        if(n*9 < sum):
            return "-1"
        
        while(sum>0):
            if(sum >= 9):
                res += '9'
                sum = sum - 9
                n -= 1
            
            else:
                res += str(sum)
                sum = 0
                n -= 1
                
        while(n):
            res += '0'
            n -= 1
        
        return res

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
