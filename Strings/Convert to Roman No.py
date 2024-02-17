'''
    Name: Rishabh Mathur
    Date: 17th Feb, 2024
'''
class Solution:
    def convertRoman(self, n):
        #Code here
        units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]
        
        return (thousands[(n//1000)] + hundreds[(n%1000)//100] + tens[(n%100)//10] + units[(n%10)])

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ob = Solution()
        print(ob.convertRoman(n))
