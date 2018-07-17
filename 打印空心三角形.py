
#打印空心三角形

for i in range(5):
    for j in range(i+1):
        if i==4:
            print("* ",end="")
            continue
        if j==0 or j==i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()



for i in range(1,6):
    for k in range(1,6-i):
        print(end=" ")
    for j in range (6-i,6):
        if i==5 or j==6-i or j==5:
            print("* ",end="")
        else:
            print( '  ',end="")
    print()