for i in range(1,10):
    for j in range (1,10):
        if i<j:
            print("  ",end="")
        else:
            print(i,'*',j,'=',i*j,end="")
            print(end="  ")
    print()