'''
    Name: Rishabh Mathur
    Date: 3 Jun, 2024
'''

class Solution:
    def areIsomorphic(self,str1,str2):
        len1, len2 = len(str1), len(str2)
        
        if(len1 != len2):
            return False
        
        hmap = {}
        str2_hmap = set()
        
        for i in range(len1):
            char1, char2 = str1[i], str2[i]
            
            if(char1 in hmap):
                if(hmap[char1] != char2):
                    return False
                
            else:
                if(char2 in str2_hmap):
                    return False
                    
                hmap[char1] = char2
                str2_hmap.add(char2)
                    
                    
        return True

import atexit
import io
import sys
from collections import defaultdict

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
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)