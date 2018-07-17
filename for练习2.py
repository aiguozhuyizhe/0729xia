#简单打印
"""
* * * * *
*       *
*       *
* * * * *

"""
for i in range(4):
    if i ==0 or i==3:
        print("* "*5)


    if i==2 or i==1:
        for j in range(5):
            if j==0 or j==4:
              print("* ",end="")
            else:
                print("  ",end="")
        print()


