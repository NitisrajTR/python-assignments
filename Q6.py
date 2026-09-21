n=int(input('No.of years:'))
b=[]
for i in range(n):
    a=list(map(int,input('Enter the monthly rainfall for year ' + str(i+1) + ': ').split()))
    c=sum(a)/len(a)
    d=format(c,".2f")
    b.append(d)
z=int(input("which years average monthly rainfall do you want to see? "))-1
print("Average monthly rainfall for year",z+1,"is",b[z])