n=int(input())
a=list(map(int,(input().split())))
m=int(input())
b=list(map(int,(input().split())))
z=[]
y=[]
for i in a:
    z.append(i)
for i in b:
    z.append(i)
z.sort()

for i in z:
    s=0
    for j in z:
        if i==j:
            s=s+1
    if s%2!=0:
        if i in a and i in b:
            if i not in y:
                y.append(i)
y.sort()
if y:
    print(tuple(y))
else:
    print('No common elements found.')