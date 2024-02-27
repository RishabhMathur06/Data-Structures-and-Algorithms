'''
    Name: Rishabh Mathur
    Date: 27 feb, 2024
'''

class Solution:
    def josephus(self,n,k):
        #Your code here

        # "i" stores the current no of people standing in a circle.
        i = 1

        # It stores the safest position.
        ans = 0 

        while(i <= n):          # Looping till only one person is left.
            ans = (ans+k)%i
            i += 1

        return ans+1

    
if __name__ == "__main__":

    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))

    ob = Solution()

    print("Safest position not to be killed is: ", ob.josephus(n, k))