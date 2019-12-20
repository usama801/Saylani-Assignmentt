def factorial(num):
    factrial = 1
    if num < 0:
        print("Please Enter a Positive integer to get it's Factorial.")
    elif num == 0:
        print("The Factorial of ",num," is ",factrial )
    else:     
        for i in range(1,num + 1):
            factrial = factrial * i

        print("The Factorial of ",num," is ",factrial)


num = int(input("Enter Integer :- "))
factorial(num)
