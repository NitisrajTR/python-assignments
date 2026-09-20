n=int(input('Enter no.of workshops:'))
a=[]
print('List of workshops:')
for i in range(n):
    a.append(list(map(int,input().split())))
print('start time and end time:')
b=list(map(int,input().split()))
c=[]
for j in a:
    if j[0]<b[1] and j[1]>b[0]:
        c.append(j)
c.sort()
print('List of workshops that are overlapping:')
for k in c:
    print(*k)