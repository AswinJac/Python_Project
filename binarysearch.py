def binsear(arr,x):
    first=0
    last=len(arr)-1
    while(first<=last):
        mid=int((first+last)/2)
        if arr[mid]<x:
            first=mid+1
        elif arr[mid]>x:
            last=mid-1
        else:
            return 1
    else:
       return 0
arr=[]
for i in range(0,10):
    x=int(input())
    arr.append(x)
    arr[i]=int(input())
arr.sort( reverse=True)
x=44
res=binsear(arr,x)
if res==0:
    print("Search failed")
else:
    print("Search passed")