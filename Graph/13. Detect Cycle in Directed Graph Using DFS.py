'''
    Name: Rishabh Mathur
    Date: 14 June, 2024
'''

from typing import List

class Solution:
    def detectCycle(self, node, vis, pathVis, adj):
        vis[node] = 1
        pathVis[node] = 1
        
        for neigh in adj[node]:
            if(vis[neigh] == 0):
                if(self.detectCycle(neigh, vis, pathVis, adj)):
                    return True
                
            elif(pathVis[neigh]):
                return True
                
        pathVis[node] = 0
        
        return False
                
    
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        vis = [0]*V
        pathVis = [0]*V
        
        for node in range(V):
            if(vis[node] == 0):
                if(self.detectCycle(node, vis, pathVis, adj)):
                    return True
                    
        return False

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        ob = Solution()

        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)