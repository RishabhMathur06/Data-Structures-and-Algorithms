'''
    Name: Rishabh Mathur
    Date: 1 May, 2024
'''

class Solution:
    def smallestSubstring(self, S):
        zero = one = two = -1
        leng = float("inf")
        
        for i in range(len(S)):
            if(S[i] == '0'):
                zero = i
            elif(S[i] == '1'):
                one = i
            else:
                two = i
                
            if(zero!=-1 and one!=-1 and two!=-1):
                s = min(zero, one, two)
                e = max(zero, one, two)
                
                leng = min(leng, e-s+1)
                
        if(leng < float("inf")):
            return leng
            
        return -1

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)