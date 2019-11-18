l = ["Twinkle, twinkle, little star,",
         "How I wonder what you are!",
         "Up above the world so high,",
         "Line a diamond in the sky."
         ]

for i in range(4): 
    if i == 1: 
        print("       ",end="")
        
    elif i == 2 or i==3:
        print("              ",end="")
        
    print(l[i])
    if i == 3:
        for j in range(2):
            if j==1:
                 print("       ",end="")
                 print(l[j])
            else:
                print(l[j])

    
