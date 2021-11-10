def linear_search (a,x,n):
    for i in range(n):
        if a[i] == x:
            return i
    return -1

n = int(input("enter no. of elements:"))
a = list(map(int,input("enter the elements").split()))
key = int(input("enter search element"))

pos = linear_search(a,n,key)
if pos == -1:
    print("element not found")
else:
    print("element found at position ",pos + 1)
    
