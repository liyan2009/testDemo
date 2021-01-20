#! python3
#-*- coding:utf-8-*-

class a:
    def hello(self):
        print("哈哈哈")

class b(a):
    pass
A=a()
B=b()

A.hello()
print("测试的版本")
B.hello()
'''
try:
    x=int(input("输入数字"))
    y=int(input("请输入第二个数字"))
    print(x/y)
except (ZeroDivisionError,TypeError) as e:
    print(e)
'''
a=[1,2,3,4,5]
print(len(a))

