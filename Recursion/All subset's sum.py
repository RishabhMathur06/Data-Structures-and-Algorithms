'''
    Name: Rishabh Mathur
    Date: 28 feb, 2024
'''


class Solution:
    def cal(self, idx, res, arr, N, ans):
        
        if(idx == N):
            ans.append(res)
            return
        
        # Include the current element and move forward.
        self.cal(idx+1, res+arr[idx], arr, N, ans)
        # Do not include current element and move forward.
        self.cal(idx+1, res, arr, N, ans)
        
    def subsetSums(self, arr, N):
        # code here
        ans = []

        self.cal(0, 0, arr, N, ans)

        return ans

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")
