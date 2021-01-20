#coding='utf-8'
import requests
'''
def loginTrue():
    authenticate={'mobile': '18502038639', 'password': '1234567'}
    url='https://saas-api.mayitest.cn/user/users/authenticate'
    r=requests.post(url,data=authenticate)
    print(r.text)
    print(r.status_code)

loginTrue()
def case1(username):
    #print("\n hello world "+username.title())
    return username.title()
a=case1('username')
print(a)
'''
def get_formatted_name(first_name,las_name,middle_name=''):
    if(middle_name):
        full_name=first_name+" "+middle_name+" "+las_name
    else:
        full_name=first_name+" "+las_name
    return full_name
print(get_formatted_name("a","b"))
'''
def zdy(*n):
    print(n)
'''
