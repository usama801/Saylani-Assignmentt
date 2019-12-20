def CountLettersCase(string):
    UpperCase = 0
    LowerCase = 0
    for i in string:
        if i.isupper():
            UpperCase = UpperCase + 1
        elif i.islower():
            LowerCase = LowerCase + 1
        else:
            pass
    
    print("Total no: of Capital Letters : ",UpperCase," \nTotal no: of Small Letters : ",LowerCase)
    

string = str(input("Enter a String :- "))
CountLettersCase(string)
