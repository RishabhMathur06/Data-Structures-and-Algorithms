'''
    Name: Rishabh Mathur
    Date: 22 May, 2024
'''

class Solution:
    def check(self, start, V, adj, color):
        color[start] = 0
        
        q = []
        q.append(start)
        
        while(q):
            node = q.pop(0)
            
            for neighbour in adj[node]:
                if(color[neighbour] == -1):
                    color[neighbour] = not color[node]
                    q.append(neighbour)
                    
                elif(color[neighbour] == color[node]):
                    return False
                    
        return True
    
    def isBipartite(self, V, adj):
        #code here
        color = [-1] * V
        
        for i in range(len(color)):
            if(color[i] == -1):
                if(self.check(i, V, adj, color) == False):
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
