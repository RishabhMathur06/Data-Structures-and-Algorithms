'''
    Name: Rishabh Mathur
    Date: 24 Mar, 2024
'''

import sys
from collections import deque
sys.setrecursionlimit(10**8)

def isSafe(grid, i, j, visited):
    return ((i >= 0) and (i < len(grid)) and (j >= 0) and (j < len(grid[0])) and (grid[i][j] and not visited[i][j]))

def BFS(grid, si, sj, visited):
    row = [-1, -1, -1, 0, 0, 1, 1, 1]
    column = [-1, 0, 1, -1, 1, -1, 0, 1]

    q = deque()
    q.append([si, sj])
    visited[si][sj] = True

    while len(q) > 0:
        temp = q.popleft()
        i = temp[0]
        j = temp[1]

        for k in range(8):
            if isSafe(grid, i + row[k], j + column[k], visited):
                visited[i + row[k]][j + column[k]] = True
                q.append((i + row[k], j + column[k]))

class Solution:
    def numIslands(self,grid):
        visited = [[False for i in range(m)] for j in range(n)]
        islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    BFS(grid, i, j, visited)
                    islands += 1

        return islands

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
