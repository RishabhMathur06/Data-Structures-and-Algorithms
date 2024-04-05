'''
    Name: Rishabh Mathur
    Date: 5 Apr, 2024
'''

#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        hmap = {}
        maxFreq = 0
        
        result = []
        
        for score in arr:
            hmap[score] = hmap.get(score, 0) + 1
            maxFreq = max(maxFreq, hmap[score])
        
        for score, freq in hmap.items():
            if(freq == maxFreq):
                result.append(score)

        result.sort()
        
        return result[0], maxFreq

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
