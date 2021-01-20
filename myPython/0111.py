#coding='utf-8'
import os
'''a=10
b=20
nums=[1,2,30,40,20]
if a in nums:
    print("%d在变量集合中"%a)
else:
    print("%d不在变量集合中"%a)

'''
'''
a=[1,3,5]
b=a[:]
print(b)
print(a is b)
a='22222d'
b='22222d'
print(a is b)
#操作文件
def sum(a,b):
    return a+b
print(sum(2,5))
'''
#区分break continue,break
#break是跳出整个循环，continue继续执行，paas没有任何作用，占位符
'''str='python'
for letter in str:
    if letter=='h':
        continue
        print("继续执行")
    print(letter)
print("测试continue")
for letter in str:
    if letter=='h':
        break
        print("继续执行")
    print(letter)
print("测试执行break")
for letter in str:
    if letter=='h':
        pass
        print("继续执行")
    print(letter)
print("pass")
#中文的解决办法
print("你好，世界")'''
#操作日期和时间
'''
import time

#转化为本地时间
format='%Y-%m-%d %X'
print(time.localtime(time.time()))
print(time.strftime(format,time.localtime()))
print(time.strftime(format,time.gmtime()))

'''

#如何写主函数,会被执行的
'''if __name__=='__main__':
    time.sleep(1)
    print('clock1%s'%time.clock())
    time.sleep(1)
    print('clock2%s'%time.clock())

print(time.ctime())
'''

#学习异常处理和文件的读写功能
#一行一行的读取文件内容
#method1 这种写法被抛弃
def readfile():
    f=open("c:\\个人资料\\my.txt")
    line=f.readline()
    while line:
        print(line,end='')
        line=f.readline()
    f.close()
#print("测试打印")
#readfile()
#打开文件并读取文件的内容
#method2  一次性读取所有
def readf():
    f=open("c:\\个人资料\\my.txt")
    lines=f.readlines()
    for line in lines:
        print(line)
    f.close()#一定要关闭文件
#把一个文件里的内容写到另外一个文件
def mycopy():
    f1=open("c:\\个人资料\\my.txt")
    result=list()
    lines=f1.readlines()
    for line in lines:
        line=line.strip()
        if (len(line)==0 or line.startswith("#")):
            continue
            print("呵呵%s"%line)
        result.append(line) #获取文件里的值
    #result.sort()
    f1.close()
    print(result)
    with open("c:\\个人资料\\you.txt","w") as aw :
        aw.write("%s"%"\n".join(result))
#对字典进行排序
dict={"a":"1a","b":"2b","c":"3c"}
#print(":".join(dict))

str1='hello world'
#print(':'.join(str1))

str2=['hello','world']
#print(':'.join(str2))

str3=('hello','world')
#print(':'.join(str3))
#print(os.path.join('/hello/','world/','liyan'))

str='abc'
print(str.upper())
print(str.capitalize())
print(str.rjust(20))
print(str.ljust(20))

str='abc    '
print('像右边去除空格%s'% str.rstrip())
#文件的一系列操作：创建、修改、删除
#os.name 获取操作系统

