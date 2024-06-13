'''
    Name: Rishabh Mathur
    Date: 13 Jun, 2024
'''

class Solution:
    def maxSum(self, n): 
        pre = [0] * (n+1)
        
        for i in range(0, n+1):
            Sum = pre[i//2] + pre[i//3] + pre[i//4]
            
            if(Sum > i):
                pre[i] = Sum
                
            else:
                pre[i] = i
                
        return pre[n]

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))