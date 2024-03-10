'''
    Name: Rishabh Mathur
    Date: 10 Mar, 2024
'''

def mergeList(head1, head2):
    # Code here
    h1 = head1
    h2 = head2
    temp = None
    
    while(h1 and h2):
        temp = h2.next
        h2.next = h1.next
        h1.next = h2
        h1 = h2.next
        h2 = temp
        head2 = temp
        
    return [head1, head2]

class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
    while head:
        print(head.data, end=' ')
        head=head.next
    print()

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        head = mergeList(head1, head2)
        printList(head[0])
        printList(head[1])
