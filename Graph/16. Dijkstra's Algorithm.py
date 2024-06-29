'''
    Name: Rishabh MAthur
    Date: 29 June, 2024
'''
from collections import deque

class Solution:
    def dijkstra(self, V, adj, S):
        dist = [float("inf")]*V
        
        q = deque()
        
        dist[S] = 0
        q.append(S)
        
        while(q):
            node = q.popleft()
            
            for neighbour in adj[node]:
                nextNode = neighbour[0]
                nextDist = neighbour[1]
                
                if(dist[node] + nextDist < dist[nextNode]):
                    dist[nextNode] = dist[node] + nextDist
                    q.append(nextNode)
                    
        return dist

import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()