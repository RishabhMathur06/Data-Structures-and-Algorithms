'''
    Name: Rishabh Mathur
    Date: 4th Jun, 2024
'''

class Solution:
    def minIndexChar(self,Str, pat):
        minm = float("inf")
        seen = set()
        hmap = {}
        
        for char in Str:
            if(char not in seen):
                seen.add(char)
                hmap[char] = Str.index(char)
            
        for char in pat:
            if(char in hmap):
                minm = min(hmap[char], minm)
                
        return -1 if minm==float("inf") else minm

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
        s=str(input())
        p=str(input())
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        print(ans)