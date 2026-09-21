n=int(input("Enter no.of elements:"))
a=list(map(int,(input('Enter the numbers separated by space: ').split())))
k=int(input("Enter Start place:"))
m=int(input("Enter End place:"))
z=m-n-1
y=k-n-2
b=a[z:y:-1]
print('reversed:',*b)
print('Maximum:',max(b))
print('Minimum:',min(b))