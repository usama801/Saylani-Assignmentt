print("_________Enter Your Marks Of Various Subjects___________ \n")
eng = int(input("Enter The Marks Of English \n"))
phy = int(input("Enter The Marks Of Physics \n"))
chem = int(input("Enter The Marks Of Chemistry \n"))
math = int(input("Enter The Marks Of Math \n"))
bio = int(input("Enter The Marks Of Biology \n"))

obtained = eng+phy+chem+math+bio
total = 500
perc = (obtained/total)*100

print("Your Total Marks is: ",obtained)
print("Your Percentage is: ",perc)

if perc >90:
    print("Your Grade is __A+__")
elif perc > 80 and perc < 90:
    print("Your Grade is __A__")
elif perc > 70 and perc < 80:
    print("Your Grade is __B__")
elif perc > 60 and perc < 70:
    print("Your Grade is __C__")
elif perc > 50 and perc < 60:
    print("Your Grade is __D__")
else:
    print("Your Result is FAIL")
            
