# ！python3

from selenium import webdriver
import time
import math

# drive = webdriver.Chrome()


# drive.get("http://www.baidu.com")
list1=[1,2,4,5]
list2=[]
def hell(x):
    return x*x
#左三角
def pro1():
    for k in range(1,10):
        for i in range(1,k+1):
            print("%d*%d=%d" % (k,i,k*i),end=" ")
        print(" ")


#右三角
def pro1r():
    for k in range(1,10):
        for j in range(1,10-k):
            print(end="       ")
        for i in range(1,k+1):
            print("%d*%d=%2d" % (k,i,k*i),end=" ")
        print(" ")
pro1r()


