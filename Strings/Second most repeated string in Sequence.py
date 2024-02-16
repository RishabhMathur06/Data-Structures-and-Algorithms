'''
    Name: Rishabh Mathur
    Date: 16th Feb, 2024
'''

class Solution:
    def secFrequent(self, arr, n):
        # code here
        dict = {}
        
        for i in arr:
            if (i not in dict):
                dict[i] = 1
            else:
                dict[i] += 1
            
        l = []
        
        for i in dict:
            l.append(dict[i])
            
        l.sort()
        
        a = l[-2]
        
        return list(dict.keys())[list(dict.values()).index(a)]
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
