'''
    Name: Rishabh MAthur
    Date: 4 May, 2024
'''

class Solution:
    def rearrange(self,arr, n):
        # code here
        arr_pos = []
        arr_neg = []
        
        for i in range(n):
            if (arr[i] >= 0):
                arr_pos.append(arr[i])
            
            else:
                arr_neg.append(arr[i])
                
        i = 0
        pos = 0
        neg = 0
        
        while(i<n):
            if (pos < len(arr_pos)):
                arr[i] = arr_pos[pos]
                pos += 1
                i += 1
                
            if (neg < len(arr_neg)):
                arr[i] = arr_neg[neg]
                neg += 1
                i += 1
            
        return arr

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1
