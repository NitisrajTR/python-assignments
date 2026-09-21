a=list(map(int,(input('Enter the numbers separated by space: ').split())))
n=len(a)
b=[]
if a[0]>a[1]:
    b.append(a[0])
for i in range(n):
    if i>0 and i<n-1:
        if a[i]>a[i-1] and a[i]>a[i+1]:
            b.append(a[i])
if a[-1]>a[-2]:
    b.append(a[-1])
print('Peaks:',b)