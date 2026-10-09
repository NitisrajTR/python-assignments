n=int(input())
a=list(map(int,(input().split())))
b=[]
for i in range(len(a)-1):
    z=a[i]-a[i+1]
    if z<0:
        z=(-1)*z
    b.append(z)
c=tuple(b)
print(c)