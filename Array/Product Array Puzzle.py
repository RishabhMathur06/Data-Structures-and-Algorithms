'''
    Name: Rishabh Mathur
    Date: 21 Feb, 2024
'''

class Solution:
    def calcProdArr(self, nums, n):
        # Initialize the product of all elements in array as 1.
        prod = 1

        for i in nums:
            prod *= i

        for i in nums:
            print(int(prod*(i**-1)), end = " ")

if __name__ == "__main__":
    ob = Solution()

    nums = [10, 3, 5, 6, 2]
    n = len(nums)

    print("\nThe product array is: \n")
    ob.calcProdArr(nums, n)