'''
    DATE: 25 Jan, 2024
    NAME: Rishabh Mathur
'''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import deque

class Solution:
    def sieve_of_eratosthenes(self, limit):
        # Implementation of the Sieve of Eratosthenes algorithm to find primes up to a given limit
        is_prime = [True for _ in range(limit + 1)]
        is_prime[0] = is_prime[1] = False
        
        for num in range(2, int(limit**0.5) + 1):
            if is_prime[num]:
                for multiple in range(num*num, limit + 1, num):
                    is_prime[multiple] = False
        
        return is_prime

    def find_shortest_path(self, start, end):
        # BFS to find the shortest path from start to end
        queue = deque()
        queue.append([start, 0])
        visited = {start}
        
        while queue:
            current_number, level = queue.popleft()
            
            if current_number == end:
                return level
            
            for digit_index in range(4):
                for new_digit in range(10):
                    # Avoid leading zeros
                    if not digit_index and not new_digit:
                        continue
                    
                    new_number = current_number[:digit_index] + str(new_digit) + current_number[digit_index+1:]
                    if new_number == end: return level+1
                    
                    # Skip if the number has been visited before
                    if new_number in visited:
                        continue
                    
                    # Skip if the new number is prime
                    if self.is_prime[int(new_number)]:
                        visited.add(new_number)
                        queue.append([new_number, level + 1])
        
        # If end is not reachable from start
        return -1

    def solve(self, num1, num2):
        # Set a limit for prime numbers
        prime_limit = 10000

        # Get primes using the Sieve of Eratosthenes
        self.is_prime = self.sieve_of_eratosthenes(prime_limit)

        # Convert input numbers to strings
        num1_str = str(num1)
        num2_str = str(num2)

        # Find the shortest path from num1 to num2
        result = self.find_shortest_path(num1_str, num2_str)

        return result


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(num1,num2))
# } Driver Code Ends