# -*- coding: utf-8 -*-

from ftplib import FTP
ftp = FTP()
ftp.connect("61.164.55.184", 8821)
ftp.login("hzftp", "hzftp@2020")
ftp.encoding = 'utf-8'
sum1 = 0
sum2 = 0
value = 0


def search_file(start_dir):
    ftp.cwd(start_dir)
    print(ftp.pwd())

    dir_res = []
    ftp.dir('.', dir_res.append)  # 对当前目录进行dir()，将结果放入列表
    for i in dir_res:
        if i.startswith("d"):
            global sum1
            sum1 += 1
            search_file(ftp.pwd() + "/" + i.split(" ")[-1])
            ftp.cwd('..')
        else:
            global sum2, value
            sum2 += 1
            val = i.split(" ")[-2]
            value += ftp.size(val + ' ')
            if ftp.pwd().endswith('/'):
                #    print ftp.pwd()+val+"  "+str(ftp.size(val))+" B" #打印出每个文件路径和大小
                pass
            else:
                #    print ftp.pwd()+"/"+val+"  "+str(ftp.size(val))+" B"
                pass


def sum_file(file_path):
    search_file(file_path)
    print("folder number is " + str(sum1) + ", file number is " + str(sum2) + ", Totle size is " + str(value) + " B")



if __name__ == '__main__':
    sum_file("/")