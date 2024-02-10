'''
    DATE: 8th Feb, 2024
    NAME: Rishabh Mathur
'''

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
import sys

# Increase recursion limit, use with caution
sys.setrecursionlimit(100000000)

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        if not head or not head.next:
            return head
    
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
    
        return new_head

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        printList(newHead)
