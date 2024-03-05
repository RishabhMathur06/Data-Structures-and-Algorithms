''' 
    Name: Rishabh Mathur
    Date: 5 Mar, 2024
'''

#User function Template for python3
class Solution:
        def print2largest(self,arr, n):
            largest = arr[0]
            second_largest = -1

            for i in arr:
                if i > largest:
                    largest = i  

            for j in arr:
                if (j>second_largest and j<largest):
                    second_largest = j

            return second_largest

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1
