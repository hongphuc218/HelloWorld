month = int(input("What is the month?"))
if month < 1:
    print("NOTFOUND")
elif month < 4:
    print("Spring")
elif month < 7:
    print("Summer")
elif month < 10:
    print ("Autumn")
elif month < 13:
    print("Winter")
else:
    print("NOTFOUND")
    