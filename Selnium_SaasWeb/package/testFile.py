#! python3
import  os,shutil
import send2trash

'''导入需要的文件包'''
# os.chdir('C:\\')
# shutil.copy('c:\\Setup.log','d:\\test')
# shutil.copy('c:\\Setup.log','d:\\test\\test1.log')
def test(self):
    os.chdir('D:\\')
    bconFile=open('D:\\bacon.txt','a')
    bconFile.write('a  b c')
    bconFile.close()
    send2trash.send2trash('D:\\bacon.txt')

def readFile():
    for foldname,sunfoldname,filenames in os.walk('D:\\test'):
        print(foldname)
        for a in sunfoldname:
            print('foldname  is '+ foldname + '\\'+ a)
        for filename in filenames:
            print('filename is '+ filename)
        print('')
readFile()


