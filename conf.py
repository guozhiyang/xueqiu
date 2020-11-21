# _*_ coding:utf-8 _*_
import os, json, hashlib, sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
userdb_file = "./userdb"



# print(userdb_file)
def userdb_set():
    if os.path.isfile(userdb_file):
        # print(userdb_file)
        return userdb_file
    else:
        print('请先为您的服务器创建用户！')
        user_data = {}
        dict = {}
        Exit_flags = True
        while Exit_flags:
            username = input("Please input username:")
            if username != 'exit':
                password = input("Please input passwod:")
                if password != 'exit':
                    user_data.update({username: password})
                    m = hashlib.md5()
                    # m.update('hello')
                    # print(m.hexdigest())
                    for i in user_data:
                        # print(i,user_data[i])
                        m.update(user_data[i].encode())
                        dict.update({i: m.hexdigest()})
                else:
                    break
            else:
                break
        f = open(userdb_file, 'w')
        json.dump(dict, f)
        f.close()
    return userdb_file

if __name__ == '__main__':
    userdb_set()