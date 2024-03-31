'''
    Name: Rishabh Mathur
    Date: 28 Mar, 2024
'''
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # Initialize the queue with all initial rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # Adding the time as well
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges initially, return 0
        if fresh_count == 0:
            return 0
        
        # Perform BFS to rot the oranges
        while queue:
            i, j, time = queue.popleft()
            
            # Update the minutes if necessary
            if time > minutes:
                minutes = time
            
            # Check all four adjacent cells
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    # Rot the fresh orange and add it to the queue
                    grid[ni][nj] = 2
                    queue.append((ni, nj, time + 1))
                    fresh_count -= 1
        
        # If there are any fresh oranges left, return -1
        if fresh_count > 0:
            return -1
        
        return minutes

from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)
