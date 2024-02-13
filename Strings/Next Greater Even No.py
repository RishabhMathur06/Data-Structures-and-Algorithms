'''
    Date: 13 Feb, 2024
    Name: Rishabh Mathur
'''

class Solution:
    def next_permutation(x):
            ind=-1
            for i in range(len(x)-2,-1,-1):
                if int(x[i])<int(x[i+1]):
                    ind=i
                    break
                
            if ind==-1:
                return -1
                
            for i in range(len(x)-1,-1,-1):
                if int(x[i])>int(x[ind]):
                    x[i],x[ind]=x[ind],x[i]
                    break
                
            i=ind+1
            j=len(x)-1
            while i<j:
                x[i],x[j]=x[j],x[i]
                i+=1
                j-=1
            return x
    
    def getNextEven(self,x):
    	# Your code goes here       
        x=[el for el in x]
        while True:
            x = self.next_permutation(x)
            if x==-1:
                return -1
            ans=''.join(x)
            if int(ans)%2==0:
                return ans
	
if __name__ == '__main__':
    
    ob = Solution()

    x = "34722641"
    ob.getNextEven(x)