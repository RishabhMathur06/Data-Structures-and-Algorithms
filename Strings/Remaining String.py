'''
    Name: Rishabh Mathur
    Date: 6 June, 2024
'''

class Solution:
    def printString(self, S, ch, count):
        i = 0
            
        while(i<len(S) and count):
            if(S[i]==ch):
                count -= 1
            i += 1
            
        if(i==len(S) or count!=0):
            return "Empty string"
        
        return S[i:]

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ch = input()[0]
		count = int(input())
		ob = Solution()	
		answer = ob.printString(s,ch,count)
		
		print(answer)