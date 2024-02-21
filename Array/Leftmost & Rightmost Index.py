'''
    Name: Rishabh Mathur
    Date: 21 Feb, 2024
'''
class Solution:
    def indexes(self, v, x):
        # Your code goes here
        first, second = -1, -1
        
        n = len(v)

        for i in range(n):
            if v[i] == x:
                first = i
                break
                
        for i in range(n-1, -1, -1):
            if (v[i] == x):
                second = i
                break
                
        return (first, second)

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


if __name__ == "__main__":
    main()
