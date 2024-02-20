'''
    Name: Rishabh Mathur
    Date: 20th Feb, 2024
'''

class Solution:
    def duplicates(self, arr, n): 
    	# code here
            hashmap = {}
            ans = []
            
            for i in range(n):
                if arr[i] in hashmap:
                    hashmap[arr[i]] += 1
                    
                else:
                    hashmap[arr[i]] = 1
                    
            for i in hashmap.keys():
                if hashmap[i] > 1:
                    ans.append(i)
                    
            if len(ans) > 0:
                ans.sort()
                
            else:
                ans.append(-1)
                
                
            return ans
    	
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()
