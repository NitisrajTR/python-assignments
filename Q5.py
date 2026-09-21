n=int(input("Enter no.of elements: "))
a=list(map(int,(input('Enter the numbers separated by space: ').split())))
m=int(input("Enter the position that to be removed: "))
b=1
for i in range(n//m):
    del(a[(m-1)*b])
    b=b+1
z=tuple(a)
print('After removing the M th elements:',z)