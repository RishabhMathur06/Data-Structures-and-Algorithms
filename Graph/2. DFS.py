'''
    Name: Rishabh Mathur
    Date: 18 Mar, 2024
'''

class Solution:
    def dfsutils(self, node, vis, adj, ans):
        vis[node] = 1
        ans.append(node)
        
        for i in adj[node]:
            if(vis[i] != 1):
                self.dfsutils(i, vis, adj, ans)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        vis = [0]*V
        ans = []
        start = 0
        
        self.dfsutils(start, vis, adj, ans)
        
        return ans

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
