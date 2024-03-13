'''
    Name: Rishabh Mathur
    Date: 13 Mar, 2024
'''

#User function Template for python3
class Solution:
	def immediateSmaller(self,arr,n):
            # code here
            stack = []
            
            stack.append(arr[0])
            
            for i in range(1, n):
                if(arr[i] < stack[-1]):
                    arr[i-1] = arr[i]
                    
                else:
                    arr[i-1] = -1
                
                stack.append(arr[i])
                
            arr[-1] =  -1
            
            return arr
     
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
