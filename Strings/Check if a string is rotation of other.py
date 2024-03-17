'''
    Name: Rishabh Mathur
    Date: 17 Mar, 2024
'''

class Solution:
    def areRotations(self,s1,s2):
        #code here
        if(len(s1) != len(s2)):
            return False
        
        s = s1 + s1
        
        if s2 in s:
            return True
            
        else:
            return False

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s1=str(input())
        s2=str(input())
        if(Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)