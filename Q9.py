n=int(input())
a=list(map(int,(input().split())))
b=[]
if n>=6:
    b.append(a[(n-6):])
    del(b[0][1])
    del(b[0][3])
elif n==5:
    b.append(a[0:4])
elif n==4:
    b.append(a[1:3])
elif n<4:
    b.append(a)
for i in b:
    for j in i:
        print(j**3)