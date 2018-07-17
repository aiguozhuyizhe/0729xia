for i in range(5):
    #总体思路，先打印一行空格，代表每一行星号前的空格
    #再不换行，打印星号
    for j in range(5-i):
        print("  ",end="")
    for m in range(i+1):
        print("* ",end="")
    print()

