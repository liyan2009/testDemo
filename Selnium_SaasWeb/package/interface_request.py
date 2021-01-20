import requests
import json


class interfaceRequest(object):

    def __init__(self,url,data,header,method,req_type):
        self.url=url
        self.data=data
        self.header=header
        self.method=method
        self.req_type=req_type

    #get的请求
    @property
    def testInterface(self):
        try:
            if(self.method=='get'):
                r=requests.get(self.url,params=self.data,headers=self.header)
                print(r.url)
                return  r

            elif(self.method=='get' and self.req_type=='Form'):
                r = requests.post(self.url, data=self.data, headers=self.header)
                return  r

            elif(self.method=='get' and self.req_type=='Json'):
                data = json.dumps(self.data)
                r = requests.post(self.url, data=self.data, headers=self.header)
                return r

        except BaseException as e:
            print("请求不能完成",str(e))


    #获取返回的状态码
    @property
    def get_stausCode(self):
        status_code=self.testInterface.status_code
        return status_code

    #把返回的乱码的值进行转换
    @property
    def get_change(self):
        r=self.testInterface
        text=r.text.encode("ISO-8859-1").decode("utf-8")
        return text

    #返回text值
    @property
    def get_text(self):
        r=self.testInterface
        text=r.text
        return text

    #返回json值
    @property
    def get_json(self):
        r=self.testInterface
        json_r=r.json()
        return json_r



#进行测试
# url="http://www.baidu.com"
# data={'wd':'python'}
# header={}
# method="get"
# req={}
#
# req=interfaceRequest(url,data,header,method,req)
# r=req.get_change
# print(r)