'''
    Date: 15 feb, 2023
    Name: Rishabh Mathur
'''

class Solution:
    def isAnagram(self,a,b):
        #code here
        n1 = len(a)
        n2 = len(b)
        
        if n1==0 or n2==0:
            return True
            
        if sorted(a)==sorted(b):
            return True
            
        else:
            return False

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
