'''
    Date: 10th Feb, 2024
    Name: Rishabh Mathur
'''

class Solution:
    def removeDup(self, str):
        ans = ""

        for i in str:
            if i not in ans:
                ans += i
                
        # Returning answer
        return ans

if __name__ == "__main__":

    str = "geEksforGEeks"

    ob = Solution()

    answer = ob.removeDup(str)
    print(answer)
