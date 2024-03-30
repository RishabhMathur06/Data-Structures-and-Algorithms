'''
    Name: Rishabh Mathur
    Date: 30 Mar, 2024
'''

class Solution:
    def findExtra(self,a,b,n):
        #add code here
        for i in range(n-1):
            if(a[i] != b[i]):
                return i
                
        return n-1

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
