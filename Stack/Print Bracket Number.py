'''
    Name: Rishabh Mathur
    Date: 13 Mar, 2024
'''

class Solution:
	def bracketNumbers(self, S):
		# code here
		stack = []
		count = 0
		ans = []
		
		for i in S:
			if(i == "("):
				count += 1
				ans.append(count)
				stack.append(count)
				
			if(i == ")"):
				ans.append(stack.pop())
		        
		return ans


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.bracketNumbers(S)
		for value in answer:
			print(value, end = " ")
		print()
