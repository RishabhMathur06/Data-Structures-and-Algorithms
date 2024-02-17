'''
    Name: Rishabh Mathur
    Date: 17 Feb, 2024
'''
def encode(arr):
    # Code here
    n = len(arr)
    i = 0
    
    ans = ""
    count = 1
    
    while(i < n-1):
        
        if(arr[i] == arr[i+1]):
            count += 1
            i += 1
            
        else:
            ans += arr[i]
            ans += str(count)
            count = 1
            i += 1
        
    ans += arr[n-1]
    ans += str(count)
    
    return ans
#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends