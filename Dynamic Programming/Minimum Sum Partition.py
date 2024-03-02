'''
    Name: Rishabh Mathur
    Date: 2 Mar, 2024
'''
      
def calculate_sum(self, arr, n):
        sum = 0
        for i in range(n):
            sum += arr[i]
        return sum

def subset_sum(self, arr, sum, n):
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    
    for i in range(sum + 1):
        t[0][i] = False
        
    for i in range(n + 1):
        t[i][0] = True
        
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - arr[i - 1]]
            else:
                t[i][j] = t[i - 1][j]
    return t

def minDifference(self, arr, n):
    sum = self.calculate_sum(arr, n)
    t = self.subset_sum(arr, sum, n)
    mn = float('inf')
    for i in range(sum // 2 + 1):
        if t[n][i]:
            mn = min(mn, sum - 2 * i)
    return mn

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ans = minDifference(arr, N)
		print(ans)
