'''
    Name: Rishabh Mathur
    Date: 20th Feb, 2024
'''

class Solution:
    def leaders(self, A, N):
        #Code here
        maxm = A[-1]
        ans = []
        
        for i in range(N-1, -1, -1):
            if A[i] >= maxm:
                ans.append(A[i])
                maxm = A[i]
                
        ans.reverse()
        
        return ans
    
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
