#Fitting The Array
def fit(a,b):
    t=0
    a.sort()
    b.sort()
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]>b[i]:
                t=0
                break
            else:
                t=1
                break
    if t:
        print('YES')
    else:
        print('NO')
n=int(input("Size: "))
m=int(input("Size: "))
arr=[]
brr=[]
for i in range(n):
    arr.append(int(input("Value: ")))
for j in range(m):
    brr.append(int(input("Value: ")))
ans=fit(arr,brr)
