'''
    Name: Rishabh Mathur
    Date: 1 Aug, 2024
'''

class Solution:
    def lenOfLongSubarr (self, arr, n, k):
        curr_sum = 0
        sum_map = {}
        
        max_len = 0
        curr_sum = 0
        
        for i in range(n):
            curr_sum += arr[i]
            
            if(curr_sum == k):
                max_len = i + 1
                
            if(curr_sum - k in sum_map):
                max_len = max(max_len, i-sum_map[curr_sum-k])
                
            if(curr_sum not in sum_map):
                sum_map[curr_sum] = i
                
        return max_len

for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))
