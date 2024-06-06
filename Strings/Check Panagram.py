'''
    Name: Rishabh Mathur
    Date: 6 June, 2024
'''

class Solution:
    def checkPangram(self,s):
        alphabet_freq = [0 for _ in range(26)]
        
        for char in s.lower():
            if char.isalpha():
                alphabet_freq[ord(char)-ord('a')] += 1
                
        for freq in alphabet_freq:
            if not freq:
                return False
                
        return True

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
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)