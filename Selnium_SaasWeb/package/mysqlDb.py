#! python3
# -*- coding:utf-8 -*-

import pymysql

#链接数据库的时候，需要把vpn启动

#返回链接
def conn_sql():
    conn=pymysql.connect(host='rm-bp189e9h15aui04zn.mysql.rds.aliyuncs.com',user='jungil',passwd='new#mayi#2015',db='zidonghua_test', port=3306, charset='utf8')
    return  conn

#查询语句
def query_sql(sql):
    myconn=conn_sql()
    cursor=myconn.cursor()
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        # print("%s"%data)
        return data

    except Exception as e:
        print('aaatest %s',str(e))
    cursor.close()
    myconn.close()

#插入sql语句
def change_sql(sql):
    myconn = conn_sql()
    cursor = myconn.cursor()
    try:
        cursor.execute(sql)
        myconn.commit()
    except Exception as e:
        myconn.rollback()
    finally:
        cursor.close()
        myconn.close()


#查询数据库的实例
def select_sql(listid):
    sql="select * from half_auto where list_id in('{}')".format(listid) #进行传参
    data=query_sql(sql)
    print(data)


data=select_sql("583453")



