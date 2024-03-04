'''
    Name: Rishabh Mathur
    Date: 4 Mar, 2024
'''

class Solution:
    def findFloor(self,A,N,X):
        #Your code here
        l = []
        
        for i in A:
            if(i <= X):
                l.append(i)
                
        if not l:
            return -1
            
        maxm = max(l)
        
        return A.index(maxm)

import math

def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
