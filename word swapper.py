r = True
while r == True: 
    userInput1 = input("Please Enter First String : ")
    userInput2 = input("Please Enter Second String : ")
    num = int(input("Enter no. of characters to swap : "))
    
 
    userInput1=userInput1.replace(userInput1[0:num],userInput2[0:num])
 
    userInput2=userInput2.replace(userInput2[0:num],userInput1[0:num])
 
    print("Your first string has become :- ",userInput1)
    print("Your second string has become :- ",userInput2)
    r = input("To run the code again just type yes: ")
    if r == "yes":
        r = bool(True)
    else:
        r = bool(False)
