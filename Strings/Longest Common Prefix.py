'''
    Name: Rishabh Mathur
    Date: 15th Feb, 2024
'''

class Solution:
    def lcp(self, arr):
        n = len(arr)

        # If no element in array, return empty string.
        if (n==0):
            return ""
        
        # If only single element is present in array then it's LCP will be arr[0].
        if (n==1):
            return arr[0]
            
        # Sort the array in lexicographically order. 
        arr.sort()

        string = ""
        string = " ".join(arr[0])

        return string
        
if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]

    ob = Solution()

    ans = ob.lcp(arr)
    print(ans)
