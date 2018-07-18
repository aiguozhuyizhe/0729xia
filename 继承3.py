#子类和父类定义同一个名称变量，则优先使用子类本身
class Person():
    name = "NoNanem"
    age = 18
    __score = 0 #年龄是秘密，只能自己知道
    _petname = "sec"# 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping ....")
    def work(self):
        print("make some money")


# 父类写在括号里面
class Teachar(Person):
    teachar_id = "9527"
    name = "XIAOJIA"
    def make_test(self):
        print("attention")

#子类和父类定义同一个名称变量，则优先使用子类本身
t= Teachar()
print(t.name)#谁离我近用谁