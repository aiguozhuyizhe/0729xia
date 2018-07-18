#子类扩充父类功能案例
#人由工作的函数  老师也有工作函数，但老师工作需要讲课
class Person():
    name = "NoNanem"
    age = 18
    __score = 0 #年龄是秘密，只能自己知道
    _petname = "sec"# 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping ....")
    def work(self,adr):
        print("adr is ")
        print("make some money")


# 父类写在括号里面
class Teachar(Person):
    teachar_id = "9527"
    name = "XIAOJIA"
    def make_test(self):
        print("attention")
    def work(self,adr):
        #扩充父类的功能只需要调用父类相同的函数
         #方法1
         Person.work(self,adr)
        #方法2 super代表得到父类
       # super().work()
        #self.make_test()

t=Teachar()
t.work(" mingxi")