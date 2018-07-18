#继承中的构造函数
class Animel():
    def __init__(self):
        print(" is a  animel")
class PaxingAni(Animel):
    def __init__(self):
        print(" Paxing Dongwu")



class Dog(PaxingAni):
    #__init__就叫构造函数，构造函数是固定的，第一个参数一定是self
    # 每次实例化的时候，
    #第一个被自动调用，因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("i  am init in dog")
# 实例化的时候，自动调用了Dog的构造函数
#因为找到了构造函数，则不再查找父类的构造函数
kaka=Dog()

#猫没有写构造函数
class Cat(PaxingAni):
    pass

#此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
#在PaxingAni中查找到了构造函数，则停止向上查找
c=Cat()
