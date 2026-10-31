'''1.single ll singly
2.double ll doubly
3.circular ll

1.single ll singly

a) insert node from end
b) insert node from begin
c) delete node from begin
d) delete node from end
e) insert node by pos
f) insert node by val
g) delete node by pos
h) delete node by val   '''


#insert node from begin

'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("enter n nodes :"))
head=None
for i in range(n):
    data=int(input("enter a value :"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("single list after insertion at begin: ")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next   '''


#insert node from end

'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("enter n nodes :"))
head=None
for i in range(n):
    data=int(input("enter a value :"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode

print("single list after insertion at end: ")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next '''

#delete node at begin


##class node:
##    def __init__(self,data):
##        self.data=data
##        self.next=None
##n=int(input("enter n nodes :"))
##head=None
##for i in range(n):
##    data=int(input("enter a value :"))
##    newnode=node(data)
##    if head is None:
##        head=newnode
##    else:
##        temp=head
##        while temp.next:
##            temp=temp.next
##        temp.next=newnode
##if head is  not None:
##    head=head.next
##
##print("single list after deletion at begin: ")
##temp=head
##while temp:
##    print(temp.data,end="->")
##    temp=temp.next


#delete node at end


'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input("enter n nodes :"))
head = None

for i in range(n):
    data = int(input("enter a value :"))
    newnode = node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode

if head is not None:
    if head.next is None:
        head = None
    else:
        temp = head
        while temp.next.next:
            temp = temp.next
        temp.next = None

print("single list after deletion at end: ")
temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next  '''

#on 26-10-2026

#insert node by position in a single linked list

''' class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
n = int(input("Enter size of SLL: "))

for i in range(n):
    data = int(input("Enter value: "))
    newnode = node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode
pos = int(input("Enter Position: "))
data = int(input("Enter Value: "))
newnode = node(data)

if pos == 1:
    newnode.next = head
    head = newnode
elif pos < 1:
    print("Invalid Position")
else:
    temp = head

    for i in range(pos - 2):
        if temp is None:
            break
        temp = temp.next

    if temp is None:
        print("Invalid Position")
    else:
        newnode.next = temp.next
        temp.next = newnode
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("Tail")'''



#Delete node by value

##class node:
##    def __init__(self, data):
##        self.data = data
##        self.next = None
##head = None
##n = int(input("Enter size of SLL: "))
##for i in range(n):
##    data = int(input("Enter value: "))
##    newnode = node(data)
##
##    if head is None:
##        head = newnode
##    else:
##        temp = head
##        while temp.next:
##            temp = temp.next
##        temp.next = newnode
##value = int(input("Enter Value: "))
##if head is not None:
##    if head.data==value:
##        head=head.next
##    else:
##        temp=head
##        while temp.next and temp.next.data !=value:
##            temp=temp.next
##        if temp.next:
##            temp.next=temp.next.next
##        else:
##            print("value not found")         
##temp = head
##while temp:
##    print(temp.data, end=" -> ")
##    temp = temp.next
##print("Tail")


#Delete node by position


##class node:
##    def __init__(self, data):
##        self.data = data
##        self.next = Nones
##head = None
##n = int(input("Enter size of SLL: "))
##for i in range(n):
##    data = int(input("Enter value: "))
##    newnode = node(data)
##
##    if head is None:
##        head = newnode
##    else:
##        temp = head
##        while temp.next:
##            temp = temp.next
##        temp.next = newnode
##pos= int(input("Enter position: "))
##if pos<1 or head is None:
##    print("invalid position")
##elif pos==1:
##    head=head.next
##else:
##    temp=head
##    for i in range(pos-2):
##        if temp is None:
##            break
##        temp=temp.next
##    if temp is None or temp.next is None:
##        print("Invalid position")
##    else:
##        temp.next=temp.next.next       
##temp = head
##while temp:
##    print(temp.data, end=" -> ")
##    temp = temp.next
##print("Tail")


# Reverse a Single Linked List
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter value"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("SLL: ",end=' ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail")
#reverse the SLL
prev=None
temp=head
while temp:
    nextnode=temp.next
    temp.next=prev
    prev=temp
    temp=nextnode
head=prev
prev=None
temp=head
while temp:
    nextnode=temp.next
    temp.next=prev
    prev=temp
    temp=nextnode
head=prev
print("Reversed List:", end=' ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("tail") '''

#Singly Linked List Cycle Detection

'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter value"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("SLL: ",end=' ')
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print("Tail") '''


#reverse the SLL
'''
pos=int(input("Enter postition to connect last node and o for no cycle"))
if pos>0:
    temp=head
    count=1
    while count<pos:
        temp=temp.next
        count+=1
    cycle_node=temp
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=cycle_node
slow=head
fast=head
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        print("Cycle detected")
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        print("Cycle connects at",slow.data)
        break
else:
    print("no cycle connection detected ....")'''


# Insert at end in a Doubly linked list

'''
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
     
    def insert_end(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("Tail")
dll=Doublylinkedlist()
n=int(input("Enter number of nodes:"))
for i in range(n):
    value=int(input("Enter Value:"))
    dll.insert_end(value)
print("DLL")
dll.display()  '''

# Insert at beginning in a Doubly Linked List

'''class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return

        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("Tail")


dll = Doublylinkedlist()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter Value: "))
    dll.insert_begin(value)

print("DLL")
dll.display() '''

# Delete at end in a Doubly Linked List
'''
class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp

    def delete_end(self):
        if self.head is None:
            print("DLL is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("Tail")


dll = Doublylinkedlist()

n = int(input("Enter Number of Nodes: "))
for i in range(n):
    value = int(input("Enter Value: "))
    dll.insert_end(value)

print("Before Deletion:")
dll.display()

dll.delete_end()

print("After Deletion:")
dll.display() '''



# Delete at beginning in a Doubly Linked List
'''
class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp

    def delete_begin(self):
        if self.head is None:
            print("DLL is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("Tail")


dll = Doublylinkedlist()

n = int(input("Enter Number of Nodes: "))
for i in range(n):
    value = int(input("Enter Value: "))
    dll.insert_end(value)

print("Before Deletion:")
dll.display()

dll.delete_begin()

print("After Deletion:")
dll.display()
'''

'''
# Insert at Position in a Doubly Linked List

class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp

    def insert_pos(self, pos, data):
        newnode = node(data)

        if pos == 1:
            newnode.next = self.head
            if self.head:
                self.head.prev = newnode
            self.head = newnode
            return

        temp = self.head
        for i in range(1, pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        newnode.next = temp.next
        newnode.prev = temp

        if temp.next:
            temp.next.prev = newnode

        temp.next = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("Tail")


dll = Doublylinkedlist()

n = int(input("Enter Number of Nodes: "))
for i in range(n):
    value = int(input("Enter Value: "))
    dll.insert_end(value)

pos = int(input("Enter Position: "))
data = int(input("Enter Value to Insert: "))

dll.insert_pos(pos, data)

print("DLL")
dll.display() '''


#Circular linked list
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=newnode
        newnode.next=self.head
    def traverse(self,start):
        temp=self.head
        while temp.data!=start:
            temp=temp.next
            if temp==self.head:
                print("node not found")
                return
        first=temp
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==first:
                break
        print("back to starting node")    
c=cll()
n=int(input("enter no of nodes: "))
for i in range(n):
    c.insert(int(input("enter the value: ")))
start=int(input("enter starting point: "))
c.traverse(start)

'''

#Modify a Node in a Circular Linked List

'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=newnode
        newnode.next=self.head
    def modify(self,old,new):
        if self.head is None:
            print("cll is empty")
            return
        temp=self.head
        while True:
            if temp.data==old:
                temp.data=new
                print("node modified successfully ")
                return
            temp=temp.next
            if temp==self.head:
                break
            print("node not found")
    def traverse(self):
        if self.head is None:
            print("cll is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
                break
        print("back to head")
                
c=cll()
n=int(input("enter no of nodes: "))
for i in range(n):
    c.insert(int(input("enter the value: ")))
old=int(input("enter existing node: "))
new=int(input("enter new node: "))
c.modify(old,new)
c.traverse()
'''

#Circular Singly Linked List Operations in Python (Insert, Delete by Value, and Traverse
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            newnode.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=newnode
        newnode.next=self.head
    def delete(self,val):
        if self.head is None:
            print("cll is empty")
            return
        temp=self.head
        prev=None
        if self.head.data==val:
            if self.head.next==self.head:
                self.head=None
                return
            last=self.head
            while last.next !=self.head:
                last=last.next
            self.head=self.head.next
            last.next=self.head
            return
        while temp.next!=self.head:
            prev=temp
            temp=temp.next
            if temp.data==val:
                prev.next=temp.next
                return
        print("node not found")
            
    def traverse(self):
        if self.head is None:
            print("cll is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
                break
        print("back to head")
                
c=cll()
n=int(input("enter no of nodes: "))
for i in range(n):
    c.insert(int(input("enter the value: ")))
val=int(input("enter node to delete : "))
c.delete(val)
c.traverse()
'''







     



















