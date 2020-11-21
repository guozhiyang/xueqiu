from ftplib import FTP
import time,tarfile,os


def ftpconnect(host, port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    ftp.encoding = 'utf-8'
    return ftp

def downloadfile(ftp, remotepath, localpath):
    # 设置缓冲区的大小
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(2)
    fp.close()

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    #host,port, username, password
    #ftp = ftpconnect("61.164.55.184", 8821,"hzftp", "hzftp@2020")
    ftp = ftpconnect("127.0.0.1", 6969,"admin", "123456")

    # 返回一个文件名列表
    filename_list = ftp.nlst()
    print(filename_list)

    #下载文件，第一个是ftp服务器路径下的文件，第二个是要下载到本地的路径文件
   # downloadfile(ftp, "/HZ宣传视频.exe ", r"C:\Users\61631\Desktop\HZ宣传视频.exe")
    # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
    uploadfile(ftp, '/test测试.txt', r"C:\Users\61631\Desktop\test测试.txt")
    # ftp.close() #关闭ftp
    # #调用本地播放器播放下载的视频
    # os.system('start D:\soft\kugou\KGMusic\KuGou.exe C:\Users\Administrator\Desktop\ftp\test.mp3')

    print(ftp.getwelcome())# 打印出欢迎信息
    # 获取当前路径
    pwd_path = ftp.pwd()
    print("FTP当前路径:", pwd_path)
    # 显示目录下所有目录信息
    ftp.dir()
    # 设置FTP当前操作的路径
    #ftp.cwd('/upload/')


    # ftp.mkd('目录名')# 新建远程目录
    # ftp.rmd('目录名')  # 删除远程目录
    # ftp.delete('文件名')  # 删除远程文件
    # ftp.rename('fromname', 'toname')  # 将fromname修改名称为toname

    # 逐行读取ftp文本文件
    file = '/upload/1.txt'
    # ftp.retrlines('RETR %s' % file)
    #与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块（块大小默认为 8KB）下载的数据
    # ftp.retrbinary('RETR %s' % file)
    ftp.quit()