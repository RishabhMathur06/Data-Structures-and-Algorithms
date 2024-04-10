''' 
    Name: Rishabh Mathur
    Date: 10 Apr, 2024
'''

import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    def dfs(self, row, col, vis, grid, vector, Set, row0, col0, n, m):
        vis[row][col] = 1
        
        vector.append((row-row0, col-col0))
        
        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]
        
        for i in range(4):
            nrow = row+rows[i]
            ncol = col+cols[i]
            
            # Checking if the new node lies within the grid
            if(0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and vis[nrow][ncol]==0):
                self.dfs(nrow, ncol, vis, grid, vector, Set, row0, col0, n, m)
                
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        Set = set()
        
        vis = [[0]*(m) for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if(vis[i][j]==0 and grid[i][j]==1):
                    vector = []
                    self.dfs(i, j, vis, grid, vector, Set, i, j, n, m)
                    Set.add(tuple(vector))
                    
        return len(Set)

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))