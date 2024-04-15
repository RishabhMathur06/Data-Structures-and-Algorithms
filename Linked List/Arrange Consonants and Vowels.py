'''
    Name: Rishabh Mathur
    Date: 15 Apr, 2024
'''

class Solution:
    def is_vowel(self, ch):
        return ch in ['a', 'e', 'i', 'o', 'u']
        
    def arrangeCV(self, head):
        vowel_head = Node(-1)
        consonant_head = Node(-1)
        vowel_tail = vowel_head
        consonant_tail = consonant_head
        
        curr = head
        while curr:
            if self.is_vowel(curr.data):
                vowel_tail.next = curr
                vowel_tail = curr
            else:
                consonant_tail.next = curr
                consonant_tail = curr
            curr = curr.next
        
        vowel_tail.next = consonant_head.next
        consonant_tail.next = None
        
        return vowel_head.next


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

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
        arr = [str(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)