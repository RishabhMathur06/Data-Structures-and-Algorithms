'''
    Name: Rishabh Mathur
    Date: 22 Feb, 2024
'''
class Solution:
    def maxLen(self,arr, N):
        # code here
        dic = {0:-1}
        
        ans = 0
        cumm_sum = 0
        
        for i in range(N):
            if arr[i] == 1:
                cumm_sum += 1
            else:
                cumm_sum -= 1
                
            if cumm_sum in dic:
                length = i - dic[cumm_sum]
                ans = max(ans, length)
                
            else:
                dic[cumm_sum] = i
                
        return ans

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
