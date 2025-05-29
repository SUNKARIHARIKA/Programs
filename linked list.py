#a list is a collection of nodes
#each node is partioned into two one id data and the other is address data consist of values
#the main nessacity of list is dynamic allocation where as in array the size is fixed and we cant modify that
#the main diasvanatage of linked list is we cant access the single element that we want the accessing will be sequential
'''1.singly linked list
2.circular linked list
3.double linked list'''
#<------SINGLE LINKED LIST--->
class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
n1=Node(105)
n2=Node(106)
n3=Node(107)
print(n1) #prints the address of n1
'''n1.next=n2 # adress of n2 node is assigned to n1 node next part
n2.next=n3 # address of n3 node is assigned to n2
current=n1 #current stores the address of n1 that is first node'''
current=n1 #current stores the address of n1 that is first node
while current:
    print(current.data,end=' ')
    current=current.next



