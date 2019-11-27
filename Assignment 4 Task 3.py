start = True
while(start):

    age = int(input("Enter the age of person :- "))

    if (age < 1):
        print("You entered wrong input.")
    elif (age < 3 and age >= 1):
        ticket = "free"
        print("Your ticket Price is :- ",ticket)
    elif (age >= 3 and age <= 12):
        ticket = 10
        print("Your ticket Price is :- $",ticket)
    else:
        ticket = 15
        print("Your ticket Price is :- $",ticket)
        
    end = str(input("Enter y to continue Program again and n to close the program :- "))

    if (end == "Y" or end == "y"):
        start = True
    elif (end == "N" or end == "n"):
        start = False
    else:
        print("You didn't select any of the option from the above,so program will be run again. :P")
        start = True
        
