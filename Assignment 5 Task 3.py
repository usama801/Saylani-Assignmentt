def EvenNumbers(num):
    even_numbers = []
    for i in num:
        if i % 2 == 0:
            even_numbers.append(i)

        else:
            pass
    print("Total Even Numbers in List : ",even_numbers)

list_of_integers = []
x = int(input("Enter the Size of List :- "))
for i in range(0,x):
    print("Enter ",i+1," Number")
    list_of_integers.append(int(input()))
            
EvenNumbers(list_of_integers)
