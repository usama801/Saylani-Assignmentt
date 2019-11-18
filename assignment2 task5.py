DATA = [1,2,3,5,8,13,21,34,55,89]
k = 1
LOC = 1
MAX = DATA[1]
n = len(DATA)

while k in range(0,n+1):
    if k >= n:
        print("LOCATION:",LOC,"MAXIMUM:",MAX)
    elif MAX < DATA[k]:
        LOC = k
        MAX = DATA[k]
    k +=1

