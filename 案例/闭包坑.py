def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


print(" * "*20)
#修改后的闭包：

def count1():
    fs = []
    for i in  range(1,4):
        def f(m=i):
            return m*m
        fs.append(f)
    return  fs
f1,f2,f3=count1()
print(f1())
print(f2())
print(f3())
