'''
    Name: Rishabh Mathur
    Date: 13 Mar, 2024
'''

class Solution:
    def pairWithMaxSum(self, arr, N):
        # Your code goes here
        maxm = float("-inf")
        
        for i in range(N-1):
            if(arr[i]+arr[i+1] > maxm):
                maxm = arr[i] + arr[i+1]
                
        return maxm

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.pairWithMaxSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()
