'''
    Name: Rishabh Mathur
    Date: 9 Mar, 2024
'''

#User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head after reversing
            while(head):
                head.next, head.prev = head.prev, head.next

                # If we reach last node it's prev would be NONE.
                if(not head.prev):
                    return head     # Return the reversed LL
                
                #Else, continue moving forward.
                head = head.prev

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
  
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
   
    def push(self, new_data,tail):
        if not self.head:
            self.head=Node(new_data)
            return self.head
        Nnode=Node(new_data)
        Nnode.prev=tail
        tail.next=Nnode
        return Nnode
        
    def printList(self, node): 
        while(node is not None): 
            print (node.data,end=' ') 
            node = node.next
            
if __name__ == '__main__':
    t = int(input())                        # No. of test cases we have to run.
    
    for tcs in range(t):
        n=int(input())                      # Taking the length of LL.
        arr=[int(x) for x in input().split()]       # Inputing the LL values in an array.
        
        dll=DoublyLinkedList()              # Creating an object of DoublyLinkedList() class.
        tail=None
        
        for e in arr:
            tail=dll.push(e,tail)           # Pushing each element of array into DLL using push function.
        
        ob = Solution()
        resHead=ob.reverseDLL(dll.head)
        dll.printList(resHead)
        print()
        