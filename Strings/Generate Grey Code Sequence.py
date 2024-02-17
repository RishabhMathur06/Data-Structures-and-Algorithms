'''
    Name: Rishabh Mathur
    Date: 17 Feb, 2024
'''

class Solution:
    def funct(self, n):
        final_ans = []

        for i in range(4):
            gray = i^(i>>1)

            binary = bin(gray)

            binary = binary.replace('0b', '')

            zeros = '0'*(n - len(binary))

            final_ans.append(zeros+binary)

        return final_ans
    
if __name__ == "__main__":

    ob = Solution()

    n = 2

    print("\n\nThe gray_code sequence for n={} is: \n\n".format(n), ob.funct(n))
