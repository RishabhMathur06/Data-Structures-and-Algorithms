'''
    DATE: 10th Feb, 2024
    NAME: Rishabh Mathur
'''

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=self.head
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


# } Driver Code Ends
#User function Template for python3

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        new_node = Node(key)
        
        if(head1 is None):
            new_node.next = head1
            head1 = new_node
            return head1
            
        elif(head1.data >= new_node.data):
            new_node.next = head1
            head1 = new_node
            return head1
            
        else:
            curr = head1
            
            while(curr.next and curr.next.data < new_node.data):
                curr = curr.next
                
            new_node.next = curr.next
            curr.next = new_node
            
        return head1

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        key=int(input())
        h=Solution().sortedInsert(a.head,key)
        printList(h)

