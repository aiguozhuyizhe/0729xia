#继承中的构造函数
class Animel():
    def __init__(self):
        print(" is a  animel")
class PaxingAni(Animel):
    def __init__(self,name):
        print(" Paxing Dongwu{0}".format(name))



class Dog(PaxingAni):
    #__init__就叫构造函数，构造函数是固定的，第一个参数一定是self
    # 每次实例化的时候，
    #第一个被自动调用，因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("i  am init in dog")

d=Dog()

#此时Cat没有构造函数，查找向上
#因为PaxingAni的构造函数需要两个参数
class Cat(PaxingAni):
    pass
c=Cat(name="hahah")