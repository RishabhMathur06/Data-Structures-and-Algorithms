'''
    Name: Rishabh Mathur
    Date: 22 Feb, 2024
'''

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        hashmap = {}
        
        for i in range(n):
            if arr[i] not in hashmap.keys():
                hashmap[arr[i]] = 1
            
            else:
                hashmap[arr[i]] += 1
                
        for i in range(n):
            if hashmap[arr[i]] == 1:
                return arr[i]
                
        return 0

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
