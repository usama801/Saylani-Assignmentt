op1 = int(input("Enter First Operands  "))
opr = input("Enter Operation To Perform Select 'p' for power  ")
op2 = int(input("Enter Second Operand  "))
power = 1

if opr=='+':
    print(op1+op2,"Result")
elif opr=='-':
    print(op1-op2,"Result")
elif opr=='*':
    print(op1*op2,"Result")
elif opr=='/':
    print(op1/op2,"Result")
elif opr=='p':
    for i in range(0,op2):
        power = power*op1
        print(power,"Result")
else:
    print("Invalid Operation Performed")
