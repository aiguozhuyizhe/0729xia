#定义一个普通函数
def myF(a):
    print('In myF')
    return None
b= myF(3)
print(b)


# 函数作为返回值返回，被返回的函数在函数体内定义

def myF2():
    def myF3():
        print("In myF3")
        return 3

    return myF3


# 使用上面定义
#调用myF2,返回一个函数myF3.赋值给f3
f3=myF2()
print(type(f3))
print(f3)

f3()#函数名被赋值后可以直接调用