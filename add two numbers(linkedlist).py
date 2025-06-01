class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0
    t1 = l1
    t2 = l2
    
    while t1 or t2:
        s = carry
        if t1:
            s += t1.val
            t1 = t1.next
        if t2:
            s += t2.val
            t2 = t2.next
        current.next = ListNode(s % 10)
        carry = s // 10
        current = current.next
    
    if carry:
        current.next = ListNode(carry)
    
    return dummy.next
def create(digits):
    head=ListNode(digits[0])
    current=head
    for num in digits[1:]:
        newnode=ListNode(num)
        current.next=newnode
        current=current.next
    return head
def printRes(node):
    while node:
        print(node.val,end=' ')
        node=node.next
    print()
l1=create([2,4,3])
l2=create([5,6,4])
result=addTwoNumbers(l1,l2)
(printRes(result))