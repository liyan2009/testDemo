#! python3
#coding:utf-8

#对文件的操作
import os

print(os.getcwd())
#
# print(os.listdir(os.getcwd()))
#
# print(os.path.abspath('.'))

def new_file(test_dir):
    lists=os.listdir(test_dir)
    print(lists)
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

print(new_file('C:\\Users\\liyan\\PycharmProjects\\Selnium_SaasWeb\\package'))
#print()


f=lambda a,b:a+b
print(f(2,3))