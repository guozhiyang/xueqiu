import os, sys, json, hashlib, socketserver, time

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from conf import userdb_set


class Ftp_server(socketserver.BaseRequestHandler):
    user_home_dir = ''

    def auth(self, *args):
        '''验证用户名及密码'''
        cmd_dic = args[0]
        username = cmd_dic["username"]
        password = cmd_dic["password"]
        f = open(userdb_set.userdb_set(), 'r')
        user_info = json.load(f)
        if username in user_info.keys():
            if password == user_info[username]:
                self.request.send('0'.encode())
                os.chdir('/home/%s' % username)
                self.user_home_dir = os.popen('pwd').read().strip()
                data = "%s login successed" % username
                self.loging(data)
            else:
                self.request.send('1'.encode())
                data = "%s login failed" % username
                self.loging(data)
                f.close
        else:
            self.request.send('1'.encode())
            data = "%s login failed" % username
            self.loging(data)
            f.close
            ##########################################

    def get(self, *args):
        '''给客户端传输文件'''
        request_code = {
            '0': 'file is ready to get',
            '1': 'file not found!'
        }
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        filename = cmd_dic["filename"]
        if os.path.isfile(filename):
            self.request.send('0'.encode('utf-8'))  # 确认文件存在
            self.request.recv(1024)
            self.request.send(str(os.stat(filename).st_size).encode('utf-8'))
            self.request.recv(1024)
            m = hashlib.md5()
            f = open(filename, 'rb')
            for line in f:
                m.update(line)
                self.request.send(line)
            self.request.send(m.hexdigest().encode('utf-8'))
            print('From server:Md5 value has been sended!')
            f.close()
        else:
            self.request.send('1'.encode('utf-8'))
            ###########################################

    def cd(self, *args):
        '''执行cd命令'''
        user_current_dir = os.popen('pwd').read().strip()
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        path = cmd_dic['path']
        if path.startswith('/'):
            if self.user_home_dir in path:
                os.chdir(path)
                new_dir = os.popen('pwd').read()
                user_current_dir = new_dir
                self.request.send('Change dir successfully!'.encode("utf-8"))
                data = 'Change dir successfully!'
                self.loging(data)
            elif os.path.exists(path):
                self.request.send('Permission Denied!'.encode("utf-8"))
                data = 'Permission Denied!'
                self.loging(data)
            else:
                self.request.send('Directory not found!'.encode("utf-8"))
                data = 'Directory not found!'
                self.loging(data)
        elif os.path.exists(path):
            os.chdir(path)
            new_dir = os.popen('pwd').read().strip()
            if self.user_home_dir in new_dir:
                self.request.send('Change dir successfully!'.encode("utf-8"))
                user_current_dir = new_dir
                data = 'Change dir successfully!'
                self.loging(data)
            else:
                os.chdir(user_current_dir)
                self.request.send('Permission Denied!'.encode("utf-8"))
                data = 'Permission Denied!'
                self.loging(data)
        else:
            self.request.send('Directory not found!'.encode("utf-8"))
            data = 'Directory not found!'
            self.loging(data)
            ###########################################

    def rm(self, *args):
        request_code = {
            '0': 'file exist,and Please confirm whether to rm',
            '1': 'file not found!'
        }
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        filename = cmd_dic['filename']
        if os.path.exists(filename):
            self.request.send('0'.encode("utf-8"))  # 确认文件存在
            client_response = self.request.recv(1024).decode()
            if client_response == '0':
                os.popen('rm -rf %s' % filename)
                self.request.send(('File %s has been deleted!' % filename).encode("utf-8"))
                self.loging('File %s has been deleted!' % filename)
            else:
                self.request.send(('File %s not deleted!' % filename).encode("utf-8"))
                self.loging('File %s not deleted!' % filename)
        else:
            self.request.send('1'.encode("utf-8"))
            ########################################

    def pwd(self, *args):
        '''执行pwd命令'''
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        server_response = os.popen('pwd').read().strip().encode("utf-8")
        self.request.send(server_response)

    #############################################
    def ls(self, *args):
        '''执行ls命名'''
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        path = cmd_dic['path']
        cmd = 'ls -l %s' % path
        server_response = os.popen(cmd).read().encode("utf-8")
        self.request.send(server_response)

    ############################################
    def put(self, *args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename + '.new', 'wb')
        else:
            f = open(filename, 'wb')
        request_code = {
            '200': 'Ready to recceive data!',
            '210': 'Not ready to received data!'
        }
        self.request.send('200'.encode())
        receive_size = 0
        while True:
            if receive_size < filesize:
                data = self.request.recv(1024)
                f.write(data)
                receive_size += len(data)
            else:
                data = "File %s has been uploaded successfully!" % filename
                self.loging(data)
                print(data)
                break

                ################################################

    def mkdir(self, *args):
        request_code = {
            '0': 'Directory has been made!',
            '1': 'Directory is aleady exist!'
        }
        cmd_dic = args[0]
        self.loging(json.dumps(cmd_dic))
        dir_name = cmd_dic['dir_name']
        if os.path.exists(dir_name):
            self.request.send('1'.encode("utf-8"))
        else:
            os.popen('mkdir %s' % dir_name)
            self.request.send('0'.encode("utf-8"))

            #############################################

        def loging(self, data):
            '''日志记录'''

        localtime = time.asctime(time.localtime(time.time()))
        log_file = '/root/ftp/ftpserver/log/server.log'
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write('%s-->' % localtime + data + '\n')
            ##############################################

    def handle(self):
        # print("您本次访问使用的IP为:%s" %self.client_address[0])
        # localtime = time.asctime( time.localtime(time.time()))
        # print(localtime)

        while True:
            try:
                self.data = self.request.recv(1024).decode()  #
                # print(self.data)
                cmd_dic = json.loads(self.data)
                action = cmd_dic["action"]
                # print("用户请求%s"%action)
                if hasattr(self, action):
                    func = getattr(self, action)
                    func(cmd_dic)
            except Exception as e:
                self.loging(str(e))
                break


def run():
    HOST, PORT = '192.168.0.20', 6969
    print("The server is started,and listenning at port 6969")
    server = socketserver.ThreadingTCPServer((HOST, PORT), Ftp_server)
    server.serve_forever()


if __name__ == '__main__':
    run()
