n=int(input("Size of the first list:"))
a=list(map(int,(input("Enter the elements of the first list: ").split())))
m=int(input("Size of the second list:"))
b=list(map(int,(input("Enter the elements of the second list: ").split())))
c=[]
for i in a:
    if i not in c:
        if i in b:
            c.append(i)
print("Common elements in both lists are:", tuple(c))
