class Dog():
    #__init__就叫构造函数，构造函数是固定的，第一个参数一定是self
    # 每次实例化的时候，
    #第一个被自动调用，因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("i  am init in dog")

# 实例化的时候，括号内的参数需要跟构造函数的参数相匹配
kaka=Dog()
