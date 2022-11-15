a = int(input())
b = int(input())
c = int(input())
if (b**2-4*a*c)>=0:
    if ((-b+(b**2-4*a*c)**0.5)/(2*a)) != ((-b-(b**2-4*a*c)**0.5)/(2*a)):
        print((-b+(b**2-4*a*c)**0.5)/(2*a), (-b-(b**2-4*a*c)**0.5)/(2*a))
    else: print((-b+(b**2-4*a*c)**0.5)/(2*a))