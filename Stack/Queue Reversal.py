'''
    Name: Rishabh Mathur
    Date: 12 Mar, 2024
'''

class Solution:
    def rev(self, q):
        #add code here
        st = []
        
        while(not q.empty()):
            st.append(q.get())
            
        while(st):
            q.put(st.pop())
            
        return q

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
            
        ob = Solution()
        q=ob.rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()