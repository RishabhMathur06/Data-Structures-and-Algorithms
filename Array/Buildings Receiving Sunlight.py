'''
    Name: Rishabh Mathur
    Date: 21 Feb, 2024
'''

class Solution:
    def longest(self, arr, n):
        #Code Here
        count = 0
        
        maxm = arr[0]
        
        for i in range(n):
            if arr[i] >= maxm:
                count += 1
                
                maxm = arr[i]
                
        return count

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
