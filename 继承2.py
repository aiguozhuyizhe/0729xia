class Person():
    name = "NoNanem"
    age = 18
    __score = 0 #年龄是秘密，只能自己知道
    _petname = "sec"# 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print("Sleeping ....")



# 父类写在括号里面
class Teachar(Person):
    teachar_id = "9527"
    def make_test(self):
        print("attention")


t = Teachar()
print(id(t.name))
print(id(Teachar.name))
# 受保护不能外部访问
print(t._petname)
#公开访问私有变量，报错
#print(t.__score)

t.sleep()


print(t.teachar_id)# 调用成员变量的写法

t.make_test()  #调用函数（方法）的写法