'''
    Name: Rishabh Mathur
    DAte: 9 June,2024
'''

class Solution:
    def deleteNode(self, head, x):
        curr = head
        count = 1
        
        if(x==1):
            nhead = head.next
            nhead.prev = None
            return nhead
            
        while(curr.next.next != None):
            if(count==x-1):
                curr.next.next.prev = curr
                curr.next = curr.next.next
                return head
                
            curr = curr.next
            count += 1
        
        curr.next = None
        
        return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        pos = int(input())
        Solution().deleteNode(llist.head, pos)
        llist.printList(llist.head)
