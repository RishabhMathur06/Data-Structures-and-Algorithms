'''
    Name: Rishabh Mathur
    Date: 3 Aug, 2024
'''

class Solution:
    def deleteAlt(self, head):
        curr = head
        
        while(curr and curr.next):
            curr.next = curr.next.next
            curr = curr.next
            
        return head

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = Node(arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next
        ob = Solution()
        ob.deleteAlt(head)
        printList(head)
