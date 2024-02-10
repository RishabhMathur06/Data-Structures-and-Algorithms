# your task is to complete this Function
'''
    Date: 9th Feb, 2024
    Name: Rishabh Mathur
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        curr = head
        
        while(curr):
            
            for i in range(1, M):
                if curr is None:
                    return
                
                curr = curr.next
                
            if curr is None:
                return
            
            t = curr.next
            for i in range(1, N+1):
                if t is None:
                    break
                t = t.next
                
            curr.next = t
            curr = t

#{ 
 # Driver Code Starts
#main

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ") 
            temp = temp.next
        print("")


if __name__=='__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        m,p = list(map(int, input().strip().split()))
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        Solution().skipMdeleteN(llist.head, m, p)
        llist.printList()
        t -= 1
