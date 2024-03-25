'''
    Name: Rishabh Mathur
    Date: 24 Mar, 2024
'''
from queue import Queue

class Solution:
    def generateBin(self, N):
        q = Queue()
        ans = []

        # Putting the binary of 1 into queue.
        q.put("1")

        # Untill we generate the binary numbers of all N numbers
        while(N > 0):
            N -= 1      # Since we've already generated one.

            s = q.get()
            s_copy = s 

            ans.append(s)

            # Concatenate 0 & 1 with current binary value -> These will be the next two binary values
            # Also, put them in queue so that we can generate further values from them.
            q.put(s+"0")
            q.put(s_copy+"1")

        return ans

if __name__ == "__main__":

    ob = Solution()

    N = 5
    ans = ob.generateBin(N)

    print(ans)
