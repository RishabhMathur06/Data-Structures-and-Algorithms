'''
    Name: Rishabh Mathur
    Date: 23rd Feb, 2024
'''


class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        curr_sum = 0
        prev_sum = 0
        max_sum = float("-inf")
        
        left, right = 0, 0
        
        while(right < n):
            curr_sum += a[right]
            
            #If windows size = k
            if(right - left + 1 == k):
                max_sum = max(curr_sum, max_sum)
    
            # If window size is greater than given k
            elif(right - left + 1 > k):
                max_sum = max(curr_sum, max_sum)
                
                # Calculate the sum of to be removed elements from back
                # of the array from window
                prev_sum += a[left]
                
                left += 1
                
                # Check if the last element leads to negative impact on sum
                if (prev_sum < 0):
                    curr_sum -= prev_sum
                    max_sum = max(curr_sum, max_sum)
                    prev_sum = 0
                    
            right += 1
            
        return max_sum

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()
