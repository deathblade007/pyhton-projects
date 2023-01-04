a=input("Enter The Number:\t")
my_dict={
    "1":"One",
"2":"Two",
"3":"Three",
"4":"Four",
"5":"Five",
"6":"Six",
"7":"Seven",
"8":"Eight",
"9":"Nine"
}
print(a)
print(my_dict[a]) 
print("DONE")
l = input("Do you want to run the program again? (y/n): ")
if l == "y":
        l = bool(1)
else:
        l = bool(0)
