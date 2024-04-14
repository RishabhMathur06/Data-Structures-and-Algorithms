'''
    Name: Rishabh Mathur
    Date: 14 April, 2024
'''

class Solution:
    def minPartition(self, N):
        deno = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        n = len(deno)
        
        ans = []
        
        for i in range(n):
            while(N >= deno[i]):
                N -= deno[i]
                ans.append(deno[i])
                
        return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
