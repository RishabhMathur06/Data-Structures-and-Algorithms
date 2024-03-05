'''
    Name: Rishabh Mathur
    Date: 5 Mar, 2024
'''

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        seen = set()
        l = []
        
        # Finding the repeating number and appending it to l.
        for num in arr:
            if num in seen:
                l.append(num)
                
            else:
                seen.add(num)
                
        # Finding the msising number and appending to l
        for i in range(1, n+1):
            if i not in seen:
                l.append(i)
                
        return l

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
