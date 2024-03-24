'''
    Name: Rishabh Mathur
    Date: 24 Mar, 2024
'''

class Solution:
    def dfs(self, row, col, ans, image, newColor, init_color):
        ans[row][col] = newColor
        
        n = len(image)
        m = len(image[0])
        
        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]
        
        for i in range(4):
            new_row = row + rows[i]
            new_col = col + cols[i]
            
            if(new_row>=0 and new_row<n and new_col>=0 and new_col<m and image[new_row][new_col]==init_color and ans[new_row][new_col] != newColor):
                self.dfs(new_row, new_col, ans, image, newColor, init_color)
            
    def floodFill(self, image, sr, sc, newColor):
        ans = image
        init_color = image[sr][sc]
        self.dfs(sr, sc, ans, image, newColor, init_color)
        
        return ans

import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()