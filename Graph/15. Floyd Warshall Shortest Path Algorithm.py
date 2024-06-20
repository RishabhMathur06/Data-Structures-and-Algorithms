'''
    Name: Rishabh Mathur
    Date: 20th June, 2024
'''

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        for k in range(n):          # Intermediate nodes on the path
            for i in range(n):      # Staring source of the path
                for j in range(n):  # Destination node of the path
                
                    # If no path exists via intermediate node,
                    # then, no point of calculating minm path cost
                    # via that node.
                    if(matrix[i][k]==-1 or matrix[k][j]==-1):
                        continue
                    
                    # Measuring the path cost via intermediate node
                    curr = matrix[i][k] + matrix[k][j]
                    
                    # If no direct path exists between the nodes,
                    # without the intermediate node, then, build a new path.
                    if(matrix[i][j]==-1):
                        matrix[i][j] = curr
                        
                    # If already a path is there, calculate the minimum path by,
                    # comparing the actual and the calculated path.
                    else:
                        matrix[i][j] = min(matrix[i][j], curr)

        return matrix

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()