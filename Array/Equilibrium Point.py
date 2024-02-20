'''
    Name: Rishabh Mathur
    Date: 20th Feb, 2024
'''

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, length):
        # Your code here
        if length == 1:
            return 1
       
        left_sum, total_sum = 0, sum(A)
       
        # Iterate through the A elements to find the equilibrium point.
        for index in range(length):
            # Reduce the right sum by the current element.
            total_sum -= A[index]


            # If the left and right sums are equal, this is the equilibrium point.
            if left_sum == total_sum:
                return index + 1
           
            # Otherwise, add the current element to the left sum.
            left_sum += A[index]
       
        # If no equilibrium point is found.
        return -1

import math

def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()
