'''
    Name: Rishabh mathur
    Date: 30 Mar, 2024
'''

class Solution:
    def countOccurence(self,arr,n,k):
        max_count = n//k
        c = 0
        
        hashmap = {}
        
        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
                
        for ele, count in hashmap.items():
            if(count > max_count):
                c += 1
                
        return c

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
