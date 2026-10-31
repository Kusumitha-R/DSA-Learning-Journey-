#O(1) t,c/s=0(1) COnstant Time
'''arr = list(map(int, input("Enter elements: ").split()))
print("last element:",arr[-1])
print("first element:", arr[0])'''


#Linear time t.c-O(n) constant  s.c -O(1)
'''arr = list(map(int, input("Enter elements: ").split()))
maximum= arr[0]
for val in arr:
    if val>maximum:
        maximum= val
print("maximum:", maximum)'''




# Linear time complexity=o(n^2)  space complexity =constant=o(1)
'''n=int(input("enter the number:"))
for i in range(n):
      for j in range(n):
          for k in range(n):
               print(i,j,k,end=" ")
          print()'''

# emojii=windows+.

#Linear time t.c -0(n^2) constant s.c -0(1)
'''n = int(input("Enter the value :"))
for i in range(n):
    print("😂", end=' ')
for j in range(n):
    print("😂", end=' ')

for a in range(n):
    for i in range(n):
        print("😂", end=' ')
    print()
    for j in range(n):
        print("😂", end=' ')
    print()'''
'''n=int(input())
num=1
for i in range(n):
    for j in range(n):
        print(num,end=" ")
        num=num+1
    print()'''


'''spiral pattern'''
##n=int(input("Enter number:"))
##a=[[0]*n for _ in range(n)]
##print(a)
##left=0
##right=n-1
##top=0
##bottom=n-1
##num=1
##while top<=bottom and left<=right:
##    #top - left->right
##    for i in range(left,right+1):
##        a[top][i]=num
##        num+=1
##    top+=1
##    #right - top->bottom
##    for i in range(top,bottom+1):
##        a[i][right]=num
##        num+=1
##    right-=1
##    #bottom - right->left
##    for i in range(right,left-1,-1):
##        a[bottom][i]=num
##        num+=1
##    bottom-=1
##    #left - bottom->top
##    for i in range(bottom,top-1,-1):
##        a[i][left]=num
##        num+=1
##    left+=1
##for row in a:
##    print(' '.join(f"{x:2}" for x in row))



##Recursion : a function calling itself to solve a problem
##1. base class -- deadline
##2. iterative class -- how many times it should run
##
##1. direct recursion
##2. in-direct recursion
##3. head recursion
##4. tail recursion
##5. tree recursion
##6. nested recursion

'''direct recursion P.S: print n numbers'''
##def numbers(n):
##    if n==0:
##        return
##    print(n,end=' ')
##    numbers(n-1)
##n=int(input("enter nuber:"))
##numbers(n)


##def numbers(n):
##    if n==6:
##        return
##    print(n,end=' ')
##    numbers(n+1)
##n=int(input("enter nuber:"))
##numbers(n)

##def fact(n):
##    if n==0 or n==1:
##        return 1
##    return n*fact(n-1)
##n=int(input("enter nuber:"))
##print(fact(n))


'''in-direct recursion P.S: print n numbers'''
##def fun1(n):
##    if n>0:
##        print(n,end=' ')
##        fun2(n-1)
##def fun2(n):
##    if n!=0:
##        print(n,end=' ')
##        fun1(n-1)
##n=int(input("enter:"))
##fun1(n)

'''in-direct recursion P.S: prove that given no is even or odd'''
##def even(n):
##    if n>0:
##        return True
##    return odd(n-1)
##def odd(n):
##    if n!=0:
##         return False
##    return even(n-1)
##n=int(input("enter:"))
##if even(n):
##    print(n, "is even")
##else:
##    print(n,"is odd")


'''tree recursion'''
'''def tree(n):
    if n==-1:
        return
    print(n)
    tree(n-1)
    tree(n-1)
n=int(input("enter:"))
tree(n)'''

#math approach find out gcd
'''
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while b!=a:
    c=a%b
    a,b=b,c
print("gcd:",a)'''


#check whether the given number is prime or not
'''n=int(input("Enter a number:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(n, "is a prime number")
else:
    print(n,"is not a prime number")'''

# Brute Force Find a number in an array
#Tc=o(n) sc=o(1)

'''arr=list(map(int,input("enter a nos:").split()))
search=int(input("enter the search element:"))
found=0
for i in range(len(arr)):
         if arr[i]==search:
             print("search found at index:",i)
             found=1
             break
if not found:
    pritn("Value not in the array")'''

#Find a character in a string
#time complexity=o(n) s.c=o(1)
'''s=input("enter a word:")
char=input("enter the chracter to search:")
found=0
for i in range(len(s)):
    if s[i]==char:
        print(char,"found at:",i)
        found=1
        break
if not found:
    print(char,"not in the array:")'''
#Greddy apparoach
'''amt=int(input("enter a amount:"))
coins=[20,10,5,2,1]
cnt=0
for coin in coins:
    cnt+=amt//coin
    amt%=coin
print("Number of coins to be needed:",cnt)'''


#Backtracking -- pritn all the binary strings
'''n=int(input("Enter a number:"))
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+'0')
    backtrack(s+'1')
backtrack("")'''



#Processing of an array
'''arr=list(map(int,input("enter an element:").split()))
sum=0
for val in arr:
   # print(val,arr,end=" ")
   sum+=val
print(sum)
   for val in range(len(arr)):
        sum+=val
print(sum)'''



'''arr=list(map(int,input("enter an element:").split()))
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("Maximum:",max)
n=len(arr)
max=sorted(arr)
print(max[n-1])
min=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
    print("Minimum",min)'''



'''#revese of an array:
arr=list(map(int,input("Enter elements :").split()))
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=' ')'''


# count the even numbers and odd numbers in the array
'''
arr=list(map(int,input("Enter elements :").split()))
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)'''

'''sorted
arr[i]=arr[i+1]
if arr[i]>arr[i+1]
arr[i],arr[j]=arr[j],arr[i] '''

#sorting of arrays:
'''arr=list(map(int,input("Enter elements:").split()))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
            arr[i], arr[j]=arr[j], arr[i]
print("Sorted array is:", *arr)'''
 
#  spiral matrix clock wise
'''n=int(input("Enter size: "))
a=[[0]*n for i in range(n)]
print(a)
top=0
bottom=n-1
left=0
right=n-1
num=1
while top<=bottom and left<=right:
    #top -- left->right
    for i in range(left,right+1):
        a[top][i]=num
        num+=1
    top+=1
    #right -- top->bottom
    for i in range(top,bottom+1):
       a[i][right]=num
       num+=1
    right-=1
   #bottom -- right->left
    for i in range(right,left-1,-1):
        a[bottom][i]=num
        num+=1
    bottom-=1
    #left -- bottom->top
    for i in range(bottom,top-1,-1):
        a[i][left]=num
        num+=1
    left+=1
for row in a:
    for num in row:
        print(f"{num:3}",end=' ')
    print()'''

'''n = int(input("Enter size: "))
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

top, bottom, left, right = 0, n - 1, 0, n - 1

while top <= bottom and left <= right:
    # top row: left -> right
    for i in range(left, right + 1):
        print(a[top][i], end=' ')
    top += 1

    # right column: top -> bottom
    if top <= bottom:
        for i in range(top, bottom + 1):
            print(a[i][right], end=' ')
        right -= 1

    # bottom row: right -> left
    if left <= right and top <= bottom:
        for i in range(right, left - 1, -1):
            print(a[bottom][i], end=' ')
        bottom -= 1

    # left column: bottom -> top
    if top <= bottom and left <= right:
        for i in range(bottom, top - 1, -1):
            print(a[i][left], end=' ')
        left += 1              '''



#bubble sort
"""arr=list(map(int,input("enter elements:").split()))
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[i],arr[j+1]=arr[j+1],arr[j]
print(*arr)"""

#selection sort
"""a=list(map(int,input().split()))
n=len(a)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if a[j]<a[min_index]:
            min_index=j
        a[i],a[min_index]=a[min_index]
print(*arr)"""

#INSERTION SORT
"""a=list(map(int,input().split()))
n=len(a)
for i in range(1,n):
    k=a[i]
    j=i-1
    while j>=0 and a[j]>k:
        a[j+1]=a[j]
        j-=1
    a[j+1]=k
print(*a)"""


#Merge sort

##def mergesort(a):
##    if len(a)<=1:
##        return a
##    mid=len(a)//2
##    left=mergesort(a[:mid])
##    right=mergesort(a[mid:])
##    result=[]
##    while left and right:
##        if left[0] <right[0]:
##            result.append(left.pop(0))
##        else:
##            result.append(right.pop(0))
##    return result+left+right
##a=list(map(int,input("Enter element:").split()))
##print("Sorted array: ",mergesort(a))



#Quick sort


def quicksort(a):
    if len(a)<=1:
        return a
    pivot=a[-1]
    left=[x for x in a[:-1] if x<=pivot]
    right=[x for x in a[:-1] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
a=list(map(int,input("Enter element:").split()))
print("Sorted array: ",quicksort(a))










        


















    



















































    
    



