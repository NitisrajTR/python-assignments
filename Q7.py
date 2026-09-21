z=list(map(int,(input('Enter the coefficients a, b, c: ').split())))
a,b,c=z
D=((b**2)-(4*a*c))
if D>=0:
    q=((-b)+D**0.5)/(2*a)
    w=((-b)-D**0.5)/(2*a)
    m=(q,w)
    print('Roots are:', m)
else:
    print('Roots are imaginary')
    e=(-b)/(2*a)
    r=((-D)**0.5)/(2*a)
    t=(e,r)
    y=(e,-r)
    print('Roots as real and imaginary parts are:', t, y)