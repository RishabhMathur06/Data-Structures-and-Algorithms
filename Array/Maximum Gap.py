'''
    Name: Rishabh Mathur
    Date: 3 May, 2024
'''

#User function Template for python3
class Solution:
	def maxSortedAdjacentDiff(self,arr, n):
		arr.sort()
		max1 = 0
		
		for i in range(n-1):
			max1 = max(max1, abs(arr[i]-arr[i+1]))
		return max1

if __name__ == '__main__': 
	
	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.maxSortedAdjacentDiff(a, n)
		print(ans)
		tc=tc-1
