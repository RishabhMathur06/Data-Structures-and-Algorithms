'''
    Date: 27 feb, 2024
    Name: Rishabh Mathur
'''

class Solution:
     def __init__(self):
        self.d = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        
     def check(self, x, y, i, grid, word, v):
        if i == len(word):
            return True
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != word[i]:
            return False
        return self.check(x + v[0], y + v[1], i + 1, grid, word, v)

     def searchWord(self, grid, word):
        ans = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == word[0]:
                    for v in self.d:
                        if self.check(i, j, 0, grid, word, v):
                            ans.append([i, j])
                            break
        if len(ans) == 0:
            return [[-1]]
        return ans

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)
