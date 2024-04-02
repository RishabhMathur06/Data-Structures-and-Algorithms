'''
    Name: Rishabh Mathur
    Date: 2 Apr, 2024
'''

class Solution:
    def isSubSequence(self, A, B):
        j=0
        for i in range(len(B)):
            if(A[j]==B[i]):
                j+=1
            if(j==len(A)):
                return True
        return False

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)
