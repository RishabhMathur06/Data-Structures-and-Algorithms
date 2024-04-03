'''
    Name: Rishabh Mathur
    Date: 1 Apr, 2024
'''

from typing import List
class Solution:
    def dfs(self, v, parent, vis, adj):
        vis[v] = 1
        
        for neighbour in adj[v]:
            if (vis[neighbour] == 0):
                if(self.dfs(neighbour, v, vis, adj)):
                    return True
                    
            elif (parent != neighbour and parent != -1):
                return True
                    
        return False
	
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
        vis = [0]*V
        
        for v in range(V):
            if (self.dfs(v, -1, vis, adj)):
                return True
		    
        return False

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")
