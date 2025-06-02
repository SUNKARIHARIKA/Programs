class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
def create(digits):
    head=ListNode(digits[0])
    current=head
    for num in digits[1:]:
        newnode=ListNode(num)
        current.next=newnode
        current=current.next
    return head
def display(node):
    while node:
        print(node.val,end=' ')
        node=node.next
    print()
def reverse(l1):
    current=l1
    prev=None
    newnode=current.next
    while current:
        nextnode=current.next
        current.next=prev
        prev=current
        current=nextnode
    return prev
#reverse of the linkedlist using stack
def stackrev(l1):
    if not l1 or not l1.next:
        return l1
    stack=[]
    current=l1
    while current:
        stack.append(current)
        current=current.next
    new_head=stack.pop()
    current=new_head
    while stack:
        current.next=stack.pop()
        current=current.next
    current.next=None
    return new_head
l1=create([1,2,3,4,5])
l2=create([1,2,3,4,5])
rev=reverse(l1)
revs=stackrev(l2)
display(revs)
display(rev)
    