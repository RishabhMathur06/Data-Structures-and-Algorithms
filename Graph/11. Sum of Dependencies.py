'''
 Name: Rishabh Mathur
 Date: 30th May, 2024
'''
class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        sumOfDependencies = 0
        
        for neighbours in adj:
            sumOfDependencies += len(neighbours)
            
        return sumOfDependencies

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[[] for i in range(N)]
        s=list(map(int,input().strip().split()))
        for i in range(0,2*M,2):
            x=s[i]
            y=s[i+1]
            a[x].append(y)
        ob=Solution()
        print(ob.sumOfDependencies(a,N))