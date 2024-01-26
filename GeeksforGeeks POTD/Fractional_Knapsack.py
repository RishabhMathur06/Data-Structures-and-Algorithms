'''
    DATE: 26 Jan, 2024
    NAME: Rishabh Mathur
'''

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        sorted_items = sorted([[item.value/item.weight, item.value, item.weight] for item in arr], reverse=True)
        
        total_value = 0
        current = 0
        
        while current < n:
            if sorted_items[current][2] <= W:
                total_value += sorted_items[current][1]
                W -= sorted_items[current][2]
                
            else:
                total_value += (W * sorted_items[current][0])
                break
                
            current += 1
            
        return total_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends
