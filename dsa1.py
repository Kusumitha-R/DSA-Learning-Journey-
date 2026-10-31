

# write a program to prnt the sum of digits of a number
'''a=int(input())
sum=0
while a!=0:
    rem=a%10
    sum+=rem
    #print(rem,end="")
    a//=10
    print("sum:",sum)
    print("polymorphed to:",a)'''

#reverse  of a number with an expression
'''n=int(input())
rev=0
while n!=0:
    d=n%10
    rev=(rev*10)+d
    n//=10
print(rev)'''

#reverse a number
'''45n=int(input())
r=0
while r!=0:
    d=n%10
    print(d,end='')
    n//=10'''


n=int(input())
sum=0
copy=n
while n!=0:
    d=n%10
    sum+=d
    n//=10
if(copy%sum==0):
    print("Harshad's number")
else:
    print("Niven's number")
    

    






