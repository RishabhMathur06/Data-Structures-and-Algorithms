'''
    Name: Rishabh Mathur
    Date: 31 Mar, 2024
'''

from typing import List

class Solution:
    #Function to detect cycle in an undirected graph.
    def detectCycle(self, ele, adj, vis, queue):
        vis[ele] = 1    # Marking the current element as visited.

        queue.append((ele, -1))
        
        while queue:
            node, parent = queue.pop(0)
            
            for neighbour in adj[node]:
                if(vis[neighbour] != 1):
                    vis[neighbour] = 1
                    queue.append((neighbour, node))
                    
                elif(parent != neighbour):
                    return True
        
        return False
	
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [0]*V
        queue = []
              
        for ele in range(v):
            if(vis[ele] != 1):
                if(self.detectCycle(ele, adj, vis, queue)):
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
