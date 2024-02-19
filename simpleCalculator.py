# Database
username = "Nyota"
password = "1234"

uName = input("Enter username : ")
uPass = input("Enter password : ")


if uName == username and uPass == password:
    # print("You are logged in.")
    
    opp = input("Enter arthmetic operator : ")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    
    if opp == "+":
        print(num1 + num2)
    elif opp == "-": 
        print(num1 - num2)
    elif opp == "/":
        if(num2 != 0):
            print(num1 / num2)
        else:
            print("Infinite")
    elif opp == "*":
        print(num1 + num2)
    else:
        print("Wrong operator!!")
    
    
else:
    print("Invalid username and password!")