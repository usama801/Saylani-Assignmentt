fname = input("Enter your first name:")
lname = input("Enter your last name:")
fullname = fname+" "+lname
print(fullname)
print("Reverse order")
for i in range(len(fullname)-1,-1,-1):
    print(fullname[i],end="")
    
    

