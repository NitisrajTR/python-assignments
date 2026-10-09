n=int(input())
a=list(map(int,(input().split())))
z=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]==0:
                b=[a[i],a[j],a[k]]
                b.sort()
                if b not in z:
                    z.append(b)
z.sort()
for i in z:
    print(i)