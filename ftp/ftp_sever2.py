from pyftpdlib.authorizers import DummyAuthorizer
from  pyftpdlib.handlers  import FTPHandler
from  pyftpdlib.servers import FTPServer
# 实例化DummyAuthorizer来创建ftp用户
authorizer = DummyAuthorizer()
# 参数：用户名，密码，目录，权限
authorizer.add_user('admin', '123456', r'C:\Users\61631\Desktop\ftp', perm='elradfmwMT')
# 匿名登录
#authorizer.add_anonymous('/home/nobody')
handler = FTPHandler
handler.authorizer = authorizer
# 参数：IP，端口，handler
server = FTPServer(('0.0.0.0', 6969), handler)           #设置为0.0.0.0为本机的IP地址
server.serve_forever()