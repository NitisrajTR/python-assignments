n=int(input('no of workers:'))
a=[]
print('name of workers:')
a=input().split()
a.insert(0,a[-1])
a.insert(0,a[-2])
del a[-2:]
b=" ".join(a)
print(b)