# 继承语法
# 在Python中，任何类都有一个共同的父类叫object

class Person():
    name = "NoNanem"
    age = 0

    def sleep(self):
        print("Sleeping ....")



# 父类写在括号里面
class Teachar(Person):
    def make_test(self):
     pass


t = Teachar()
print(t.name)
print(Teachar.name)

print(t.age)
print(Teachar.age)