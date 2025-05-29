class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def insertLast(self,element):
        newnode=Node(element)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=newnode
    def insertBegin(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def delete_begin(self):
        if self.head is None:
            print('list is empty')
        else:
            current=self.head
            self.head=current.next
            print(current.data,'deleted')
            del current
    def delete_end(self):
        if self.head is None:
            print('list is empty')
        elif self.head.next==None:
            print(self.head.data,'deleted,list now empty')
            self.head=None
        else:
            prev=self.head
            current=self.head.next
            while current.next!=None:
                prev=current
                current=current.next
            print(current.data,'deleted')
            prev.next=None
    def insert_before_node(self,key,element):
        if self.head is None:
            print('there is no node to insert before insertion not possible')
        else:
            newnode=Node(element)
            current=self.head
            if current.data==key:
                newnode.next=self.head
                self.head=newnode
            else:
                while current.next and current.next.data!=key:
                    current=current.next
                if current.next:
                    newnode.next=current.next
                    current.next=newnode
                else:
                    print('node with data',key,'not found')
    def insert_after_node(self,key,val1):
        if self.head is None:
            print('not possible for insertion')
        else:
            newnode=Node(val1)
            current=self.head
            while current and current.data!=key:
                current=current.next
            if current:
                newnode.next=current.next
                current.next=newnode
            else:
                print('element',key,'is not found in list')
    def insert_at_position(self,value,pos):
        if pos<0:
            print('Invalid position')
            return
        newnode=Node(value)
        if pos==0:
            newnode.next=self.head
            self.head=newnode
            return
        current=self.head
        index=0
        while current is not None and index<pos-1:
            current=current.next
            index+=1
        if current is None:
            print('position out of bounds')
        else:
            newnode.next=current.next
            current.next=newnode
    def dsply(self):
        if self.head is None:
            print('list is empty')
        else:
            current=self.head
            while current:
                print(current.data,end=' ')
                current=current.next
            print()
    def delete_before_node(self,key):
        if self.head is None:
            print('list is empty')
        elif self.head.next is None:
            print('list has only one element not posibble')
        elif self.head.next.data==key:
            self.head=self.head.next
        else:
            prev=self.head
            current=prev.next
            while current.next and current.next.data!=key:
                prev=current
                current=current.next
            if current.next:
                print(current.data,'deleted')
                prev.next=current.next
            else:
                print('key element not found in the list')
    def delete_after_node(self,key):
        if self.head is None:
            print('list is empty')
        else:
            if self.head.next is None:
                print('list has only one element,not possible')
            else:
                current=self.head
                while current and current.data!=key:
                    current=current.next
                if current and current.next:
                    current.next=current.next.next
                else:
                    print('key element not found in the list or last element')
    def reverse(self):
        if self.head is None:
            print('list is empty')
        else:
            current=self.head
            prev=None
            while current:
                nextnode=current.next
                current.next=prev
                prev=current
                current=nextnode
            self.head=prev
            print('list reversed')
    def search(self,value):
        if self.head is None:
            print('linked list is empty')
            return
        current=self.head
        while current:
            if current.data==value:
                print('node with data',value,'found in the list')
                return
            current=current.next
        print('node with data',value,'not found in the linkedlist')
sll=SingleLinkedList()
while True:
    print('\n1.Insert@last\n2.Insert at begin\n3.delete at begin\n4.delete at end \n5.display\n6.serch an element in list\n7.insert element before node \n8.insert element after node\n9.insert element at position \n10.delete element before node\n11.delete element after node\n12.reverse the linkedlist\n13.exit')
    ch=int(input("enter choice"))
    if ch==1:
        ele=int(input('enter element'))
        sll.insertLast(ele)
    elif ch==2:
        ele=int(input('enter element'))
        sll.insertBegin(ele)
    elif ch==3:
        sll.delete_begin()
    elif ch==4:
        sll.delete_end()
    elif ch==5:
        sll.dsply()
    elif ch==6:
        ele=int(input("enter the element to search"))
        sll.search(ele)
    elif ch==7:
        key=int(input("enter the element before insertion"))
        ele=int(input("enter the value"))
        sll.insert_before_node(key,ele)
    elif ch==8:
        key=int(input("enter the element after insertion"))
        val1=int(input("enter the value"))
        sll.insert_after_node(key,val1)
    elif ch==9:
        value=int(input('enter the value to be inserted'))
        pos=int(input('enter position to be inserted'))
        sll.insert_at_position(value,pos)
    elif ch==10:
        key=int(input('enter the nodebefore delete'))
        sll.delete_before_node(key)
    elif ch==11:
        key=int(input('enter node that to be delted after'))
        sll.delete_after_node(key)
    elif ch==12:
        sll.reverse()
    elif ch==13:
        print('exiting')
        break
'''sll.insert(55)
sll.dsply()
sll.insert(56)
sll.dsply()
sll.insert(57)
sll.dsply()'''
#algorithm to insert at end
'''algorithm
step1: create a newnode with the given data
step2: if head is none(i.e linkedlist is empty) then
step3: set head to point to the newnode
step4:exit
step 5: else
step6: set current=head
step7 : repeat step 7 while current.next!=none
step8 : update current to its next
        [end of loop]
step9: set cuurent.next to the newnode
step10: exit'''
#algorithm to insert at begining
'''
step1: create newnode with the given data
step2: if head is none(i.e linked list is empty) then
step 3: set head to point to the newnode
step 4: exit
step 5:else
step 6:set newnode.next to point to head
step 7: update head=newnode
step 8:exit
'''
#algorithm to delete at begining
'''
step1:if Head is none(i.e linked list is empty) then print 'linked list is empty' &exit
step2: else: set current=head
step 3: set head to current.next
step 4: delete current and exit
'''
