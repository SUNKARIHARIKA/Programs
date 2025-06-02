class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
def mergesorted(list1,list2):
    dummy=ListNode(0)
    current=dummy
    current1=list1
    current2=list2
    while current1 and current2:
        if current1.val<=current2.val:
            current.next=current1
            current1=current1.next
        else:
            current.next=current2
            current2=current2.next
        current=current.next
    return dummy.next
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
list1=create([1,2,4,5])
list2=create([1,3,4,5,6])
node=mergesorted(list1,list2)
display(node)