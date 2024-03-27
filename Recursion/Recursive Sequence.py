'''
    Name: Rishabh Mathur
    Date: 27 Mar, 2024
'''

MOD = (10**9)+7
class Solution:
    def sequence(self, n):
        ans = 0
        last = 1
        
        for i in range(1, n+1):
            temp = 1
            
            for j in range(1, i+1):
                temp = (temp*last) % MOD
                last += 1
                
            ans = (ans+temp) % MOD
        
        return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
