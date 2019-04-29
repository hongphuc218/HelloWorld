print("ax^2 + bx + c = 0")
a = int(input("a?"))
b = int(input("b?"))
c = int(input("c?"))
if (b**2-4*a*c)<0:
    print("phuong trinh vo nghiem")
elif (b**2-4*a*c)==0:
    print("co nghiem kep la: x = ", -b/2*a)
else: