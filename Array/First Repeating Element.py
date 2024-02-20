'''
    Name: Rishabh Mathur
    Date: 20th Feb, 2024
'''
class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        hashmap = {}
        
        for i in arr:
            if i not in hashmap.keys():
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                
        for i in range(n):
            if hashmap[arr[i]] > 1:
                return i+1
                
        return -1

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
