
class Solution:
    def minDist(self, arr, n, x, y):
        x_position, y_position, min_distance = -1, -1, float("inf")
        
        for position in range(n):
            if x == arr[position]:
                x_position = position
                
            elif y == arr[position]:
                y_position = position
                
                
            if x_position != -1 and y_position != -1:
                min_distance = min(min_distance, abs(y_position - x_position))
                
        return -1 if min_distance == float("inf") else min_distance

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))

