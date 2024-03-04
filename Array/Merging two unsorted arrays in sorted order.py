'''
    Name: Rishabh Mathur
    Date: 3 Mar, 2024
'''

class Solution:
    def sortedMerge(self, a, b, res, n, m):
        a.sort()
        b.sort()
        
        i=j=k=0
        
        while(i<n and j<m):
            if(a[i] <= b[j]):
                res[k] = a[i]
                i += 1
                k += 1
            else:
                res[k] = b[j]
                j += 1
                k += 1
            
        # Do for the remaining elements left
        while(i < n):
            res[k] = a[i]
            i += 1
            k += 1
            
        while(j < m):
            res[k] = b[j]
            j += 1
            k += 1
            
        return res

if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a=list(map(int,input().split()))
        b = list(map(int, input().split()))
        c=[0]*(n+m)
        ob = Solution()
        ob.sortedMerge(a,b,c,n,m)
        for i in c:
            print(i,end=" ")
        print()
