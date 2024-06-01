'''
    Name: Rishabh Mathur
    Date: 1 June, 2024
'''

class Solution:
    def findKRotation(self,arr,  n):
        count = 0
        
        i = 0
        j = n-1
        
        while(i < j):
            if(arr[i] > arr[j]):
                count += 1
                i += 1
                
            else:
                return count
                
        return count

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1
