# Time complexity =o(1)
'''
arr=list(map(int,input("Enter the elements:").split()))
print("last element:",arr[-1])
print("First element:",arr[0])'''
# linear time=o(n) sc=o(1)
arr=list(map(int,input("enter the elements:").split()))
max=arr[0]
for val in arr:
    if val>max:
        maxium=val
print("Maximum:",maxium)





