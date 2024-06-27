'''
    Name: Rishabh Mathur
    Date: 27 June, 2024
'''

class Solution:
    def maxSumIS(self, Arr, n):
        dp = Arr[:]
        ans = Arr[0]
        
        for i in range(1, n):
            for j in range(i):
                if(Arr[i] > Arr[j] and dp[i] < Arr[i]+dp[j]):
                    dp[i] = Arr[i] + dp[j]
                    
            ans = max(ans, dp[i])

        return ans


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)