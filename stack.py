##stack data structures##
'''
insert --- push ---- append
delete -- pop --pop
to see the top element --- arr[-1]
is empty()
overflow
'''
#Stack operations push
'''stack=[]
n=int(input("Enter size:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack.append(val)
print("STACK:",stack)
print("PEEK:",stack[-1])'''

#stack operations push pop
'''
stack=[]
n=int(input("Enter size:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack.append(val)
print("STACK:",stack)
print("PEEK:",stack[-1])
if len(stack)==0:
    print("stack Empty !!!")
else:
    removed=stack.pop()
print("Stack after pop:",stack)'''
#stack operations push pop
'''
stack=[]
n=int(input("Enter size:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack.append(val)
print("STACK:",stack)

while len(stack)>0:
    removed=stack.pop()
    print(removed)
print("Stack after pop:",stack)
print("Stack Empty !!")
'''
# Stack Overflow Operation
'''
stack = []
size = int(input("Enter size: "))
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input("Enter a value: "))
    if len(stack) == size:
        print("Overflow....")
    else:
        stack.append(val)
        print(val, ": Pushed")
print("Stack:", stack)
'''

#Add two stacks[10,20]+[30,40]=[10,20,30,40]

# Stack Operations - Add Two Stacks
# Example: [10, 20] + [30, 40] = [10, 20, 30, 40]

'''
stack1 = []
stack2 = []
n = int(input("Enter number of elements of stack1: "))
for i in range(n):
    val = int(input("Enter a value: "))
    stack1.append(val)
print("Stack 1:", stack1)
n = int(input("Enter number of elements of stack2: "))
for i in range(n):
    val = int(input("Enter a value: "))
    stack2.append(val)
print("Stack 2:", stack2)
stack = stack1 + stack2
print("Total Stack:", stack)
'''
#Merge stacks [1,3,5]
#merge [2,4,6]=[1,2,3,4,5,6]

# Merge Two Sorted Stacks
'''
stack1 = []
stack2 = []

n = int(input("Enter number of elements of stack1: "))
for i in range(n):
    val = int(input("Enter a value: "))
    stack1.append(val)
print("Stack 1:", stack1)
n = int(input("Enter number of elements of stack2: "))
for i in range(n):
    val = int(input("Enter a value: "))
    stack2.append(val)
print("Stack 2:", stack2)
merged = []
i, j = 0, 0
while i < len(stack1) and j < len(stack2):
    if stack1[i] < stack2[j]:
        merged.append(stack1[i])
        i += 1
    else:
        merged.append(stack2[j])
        j += 1
merged.extend(stack1[i:])
merged.extend(stack2[j:])
print("Merged Stack:", merged)'''

'''
#inorder to preorder conversion using stacks
"""exp=input("enter a expression")
stack=[]
result=[]
priority={'+':1,'*':2,'/':2,'^':3}
rev=exp[::-1]
for ch in rev:
    if ch.isalnum():
        result.append(ch)
    elif ch==')':
        stack.append(ch)
    elif ch=='(':
        while stack and stack[-1]!=')':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1]!=')' and priority.get(stack[-1],0)>priority.get(ch,0):
            result.append(stack.pop())
        stack.append(ch)
while stack:
    result.append(stack.pop())
prefix=''.join(result[::-1])
print("prefix:",prefix)"""
    
#infix to postfix
"""exp=input("enter a expression")
stack=[]
result=[]
priority={'+':1,'*':2,'/':2,'^':3}
for ch in exp:
    if ch.isalnum():
        result.append(ch)
    elif ch=='(':
        stack.append(ch)
    elif ch==')':
        while stack and stack[-1]!='(':
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1]!='(' and priority[stack[-1]]>=priority[ch]:
            result.append(stack.pop())
        stack.append(ch)
while stack:
    result.append(stack.pop())
print(''.join(result))"""


#postfix to prefix
exp=input("enter a expression")
stack=[]
for ch in exp[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        a=stack.pop()
        b=stack.pop()
        result=ch+a+b
        stack.append(result)
print(stack[-1])
'''

s=input("enter the paranthesis: ")
stack=[]
for ch in s:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if len(stack)==0:
            print("not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("balanced")
    else:
        print("unbalanced")

    
      







