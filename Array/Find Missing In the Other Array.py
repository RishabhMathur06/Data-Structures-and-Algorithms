'''
    Name: Rishabh MAthur
    Date: 8 June, 2024
'''

class Solution:
    def findMissing(self,a,b,n,m):
        # code here
        seen = set()
        ans = []
        
        for i in range(m):
            if(b[i] not in seen):
                seen.add(b[i])
                
        for i in range(n):
            if(a[i] not in seen):
                ans.append(a[i])
                
                
        return ans

t=int(input())
for _ in range(0,t):
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()