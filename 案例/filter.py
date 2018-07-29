def isEven(a):
    return a%2==0


l = [1,2,3,4,5,6,7,8,9,10]
rst=filter(isEven,l)
print([i for i in rst])
