'''
    Name: Rishabh Mathur
    Date: 16 Feb, 2024
'''
class Solution:

    def firstRepChar(self, s):
        # code here
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 1
                
            elif i in dict and dict[i] == 1:
                return i
            
        return -1

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
