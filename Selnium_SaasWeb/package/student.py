#! python3
# -*- coding:utf-8 -*-

class Student(object):

    @property
    def score(self):
        return self.cc

    #这种设置属性，详单与是赋值
    @score.setter
    def score(self,value):
        self.cc=value


s=Student()
s.score=60

print(s.score)




