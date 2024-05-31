class Solution:
    def dfs(self, node, col, color, adj):
        color[node] = col
        
        for neighbour in adj[node]:
            if(color[neighbour] == -1):
                if(self.dfs(neighbour, not col, color, adj) == False):
                    return False
                
            elif(color[neighbour] == col):
                return False
                
        return True
    
    def isBipartite(self, V, adj):
        color = [-1] * V
        col = 0
        
        for i in range(V):
            if(color[i] == -1):
                if(self.dfs(i, col, color, adj) == False):
                    return False
                    
        return True

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")
