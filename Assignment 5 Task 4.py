def palindrome(string):
    s = ""
    for i in range(len(string),0,-1):
        s = s+string[i-1]
    print("The String after Reversing String : ",s)

    if s == string:
        print("The String you entered is Palindrome.")

    else:
        print("The String you entered is not Palindrome.")

x = input("Enter a String :- ").upper()
palindrome(x)    
