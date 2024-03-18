'''
    Name: Rishabh Mathur
    Date: 18 Mar, 2024
'''

class Solution:
    def dfs(self, node, vis, adj):
        if(vis[node] == 0):
            vis[node] = 1
            
            for i in range(len(adj[node])):
                if(adj[node][i] == 1):
                    self.dfs(i, vis, adj)
    
    def numProvinces(self, adj, V):
        # code here 
        count = 0
        vis = [0]*V
        
        for i in range(V):
            if(vis[i] == 0):
                count += 1
                self.dfs(i, vis, adj)
                
        return count

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
