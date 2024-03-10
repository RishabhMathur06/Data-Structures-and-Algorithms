'''
    Name: Rishabh Mathur
    Date: 9 Mar, 2024
'''

class Solution:
    def rearrange(self, head):
        # Code here
        if not head or not head.next:
            return head
        
        # Creating two different lists.
        head1 = head
        alt = head.next
        head2 = head1.next
        
        while head1 and head2 and head2.next:  # Update the termination condition
            head1.next = head2.next
            head2.next = head2.next.next
            
            head1 = head1.next
            head2 = head2.next
                
        # Reversing the second list
        prev = None
        nex = alt.next
        
        while alt:
            alt.next = prev
            prev = alt
            alt = nex
            if nex:
                nex = nex.next
                
        # Merging the linked lists.
        head1.next = prev
        
        return head

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
