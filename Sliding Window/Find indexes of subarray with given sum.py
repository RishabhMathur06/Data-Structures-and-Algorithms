'''
    Name: Rishabh Mathur
    Date: 22 Feb, 2024
'''

class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        curr_sum = 0
        prev_sums = {}
        
        for i in range(n):
            curr_sum += arr[i]
            
            if(curr_sum == s):
                return [1, i+1]
                
            if(curr_sum - s) in prev_sums:
                return [prev_sums[curr_sum - s]+2, i+1]
                
            prev_sums[curr_sum] = i
            
        return [-1]

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
