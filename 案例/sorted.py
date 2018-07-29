#sorted排序案例,reverse是降序排
a=[234,22313,123,45,43,2,3,66723,34]
al=sorted(a,reverse=True)
print(al)


#排序案例2
a=[-43,23,45,6,-23,2,-4345]
#按绝对值信息排序
#abs是求绝对值的意思
#即按照绝对值的倒叙（降序）排序
al=sorted(a,key=abs,reverse=True)
print(al)


#sorted案例
astr = ['dana','Danaa','wangxiaojing','jingjing','haha']
str1=sorted(astr)
print(str1)

str2=sorted(astr,key=str.lower)#将字符串转化成小写再排序
print(str2)