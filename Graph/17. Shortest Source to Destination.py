'''
    Name: Rishabh Mathur
    Date: 30 June, 2024
'''

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        if(A[0][0]==0 or A[X][Y]==0):
            return -1
            
        queue = [[0, 0]]
        path_length = 0
        
        while(queue):
            next_queue = []
            
            for row, col in queue:
                if(row<0 or row>=N or col<0 or col>=M or A[row][col]==0):
                    continue
                
                if(row==X and col==Y):
                    return path_length
                    
                A[row][col] = 0
                
                next_queue.extend([[row, col-1], [row-1, col], [row, col+1], [row+1, col]])
                
            queue = next_queue
            path_length += 1
            
        return -1

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))