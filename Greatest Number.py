num1=int(input("ENTER THE NUMBER1:\t"))
num2=int(input("ENTER THE NUMBER2:\t"))
num3=int(input("ENTER THE NUMBER3:\t"))
num4=int(input("ENTER THE NUMBER4:\t"))
if num1>num4:
    f1=num1
else:
    f1=num4
if num2>num3:
    f2=num2
else:
    f2=num3
if f1>f2:
    print(str(f1)   +  "is greatest")
else:
     print(str(f2)   +  "is greatest")
     print("DONE")
