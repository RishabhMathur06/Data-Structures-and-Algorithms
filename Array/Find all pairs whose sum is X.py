'''
    Name: Rishabh Mathur
    Date: 2 Jun, 2024
'''

class Solution:
    def allPairs(self, A, B, N, M, X):
        A.sort()
        
        res=[]
        
        for i in range(N):
            if(X-A[i] in B):
                res.append([A[i], X-A[i]])
                
        return res

def main():
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0:
            print(-1) 
         
        else:
            for i in range(sz):
                if i==sz-1:
                    print(*answer[i])
              
                else:
                    print(*answer[i], end=', ')
        
        T -= 1
        
if __name__ == "__main__":
    main()