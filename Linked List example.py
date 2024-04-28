class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insertAtEndOfTail(head,ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newBlock
    return head

def printlist(head):
#below line of code is assigning head to curr
    curr=head
#below line is checking whether curr reachedclass Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
obj1=Node(20)
print(obj1.data)

obj2=Node(30)
obj3=Node(40)
obj4=Node(50)

obj1.next=obj2
obj2.next=obj3
obj3.next=obj4

curr=obj1
while curr!=None:
    print(curr.data,end="-->")
    curr=curr.next
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next
    print()
    
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)
