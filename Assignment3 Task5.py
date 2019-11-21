

my_list = [20,30,20,30,40,50,15,11,20,40,50,70,15]
my_list.sort()
for i in range (len (my_list) -1):
    if my_list[i] == my_list[i+1]:
        print (my_list[i])
