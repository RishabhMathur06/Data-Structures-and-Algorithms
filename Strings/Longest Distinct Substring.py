'''
    Name: Rishabh Mathur
    Date: 21 Apr, 2024
'''

class Solution:

    def longestSubstrDistinctChars(self, S):
        a = {}  
    
        n = len(S)  # Get the length of the string
        j = 0  # Initialize start pointer
        m = 0  # Initialize maximum length
        
        for i in range(n):  # Iterate through each character of the string
            if S[i] in a:
                a[S[i]] += 1
            else:
                a[S[i]] = 1
            
            while a[S[i]] > 1:  # If frequency of current character becomes more than 1
                a[S[j]] -= 1
                j += 1
            
            m = max(m, i - j + 1)  # Update maximum length
            
        return m

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)
