'''
    Name: Rishabh Mathur
    Date: 5 Mar, 2024
'''

class Solution:
    def findMaximumDiff(self, a, n):
        i = 0
        j = n-1
        
        maxm = 0
        
        while(i < n and j > -1 and i <=j):
                if(a[i] <= a[j]):
                    maxm = max(maxm, j-i)
                    i += 1
                    j = n-1
                    
                else:
                    j -= 1
                
        return maxm

if __name__ == "__main__":

    a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    n = len(a)

    ob = Solution()
    print("The maximum difference is: ", ob.findMaximumDiff(a, n))