import time

#任务：
#对hello函数进行功能扩展，每次执行hello前打印当前时间

import time
#高阶函数,以函数作为参数

def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper

# 上面定义了装饰器，使用的时候需要用@，@符号是Python的语法糖
@printTime
def hello():
    print("Hello world")

hello()

#装饰器的好处是，一点定义，则可以装饰任意函数
#一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上


@printTime
def hello2():
    print("今天很高兴")
    print("还可以有很多选择")
hello2()

#上面对函数的装饰使用系统定义的语法糖
#现在开始手动执行下装饰器
#先定义函数

def hello3():
    print("我是手动执行的")
hello3()

hello3=printTime(hello3)
hello3()

b=printTime(hello3)
b()