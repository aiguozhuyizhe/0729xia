#复杂点的返回函数例子
#args:参数列表
#1  myF4定义函数，返回内部定义的函数myf5
#2  myF5使用了外部变量，这个变量是myf4的参数

def myF4(* args):#args 收集参数作用域整个函数
    def myF5():
        rst=0
        for n in args:
            rst+=n
        return rst
    return myF5

#调用
f5=myF4(1,2,3,4,5,6,7,8,9,0)
print(f5())

f6=myF4(10,20,30,40,50)
print(f6())