#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    return arr[i]

            return arr[-1]

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1
