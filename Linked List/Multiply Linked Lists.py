'''
    Name: Rishabh Mathur
    Date: 10 June, 2024
'''
MOD = 10**9+7

def multiplyTwoList(head1, head2):
    num1 = 0
    num2 = 0
    
    while(head1 is not None):
        num1 = (num1*10 + head1.data)
        head1 = head1.next
        
    while(head2 is not None):
        num2 = (num2*10 + head2.data)
        head2 = head2.next
        
    return (num1*num2)%MOD

class node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        list2 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list2.insert(i)
        print(multiplyTwoList(list1.get_head(), list2.get_head()))
