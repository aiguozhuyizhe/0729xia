import  functools
#把字符串转化成十进制数字
int('12345')
#把字符串转化成八进制整数
print(int('12345',base=8))
#或者直接int('12345',8)

print(" * "*20)
#新建一个函数，此函数是默认输入的字符串是16进制数字
#把次字符串返回十进制数字
def int16(x,base=16):
    return int(x,base)

print(int16('12345'))


print(" * "*20)
#实现上面int16的功能
int16=functools.partial(int,base=16)

print(int16('12345'))