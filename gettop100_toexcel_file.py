import sys
import time
import bs4
import requests
import os
import pandas as pd
import datetime

import time

from pythonbean.combinationBean import Combination
from pythonbean.second_copy import getResponse
from pythonbean.getRebalancestock import getRbResponse
from myfunction.common import write_excel3



def takesegment_id(elem):
    return elem.segment_id

def takecruweight(elem):
    return -float(0 if elem.weight is None else elem.weight)


def takerbsegment_id(elem):
    return -float(0 if elem.price is None else elem.price)

my_list = []

def spider_xueqiu(level=1,filename=None,downloadcount=1,sleeptime=30):
    headers = {
        'User-agent': 'Xueqiu iPhone 12.22',
        'cookie': 'xq_a_token=ef60ae661da28e68f8918bc0e0d33ca59f30a148;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjkyNjUxNzE5MjksImlzcyI6InVjIiwiZXhwIjoxNjA3NTA1MjM2LCJjdG0iOjE2MDQ5MTMyMzY3NDUsImNpZCI6IldpQ2lteHBqNUgifQ.Jq_uKZsWUM1wIp-Nni6Q2WGs1zWguHMV9WDi7lejluE-KbsxdOJU5tpXUgRsbirlbLGdx0xZ7BdZdjLlxM_w2aXgVQ0h5H3IiW6vG82bzhSm4WSZN5qs7zZs7Dg5fvLRxdVtFbmNsMKjCfSSLtGjAikgUfIyn7SMUwQVQAadz4-8-386C28nbiY0fNp8eahLkbyBgBvBDiWnQryMX_d5Ka7a2xFgZYL0e1FjF0kdvC3NR10dTCl15J04yt4RYiroVWp4-1vyb_h5RIJXEYzv2plvePRAzvbYH8B_dIcaendBVzjy-5xDXjN2EkDASq2LfiNqw_MD01sxLnq5fSuAPA;u=9265171929',
        'X-Device-ID': 'DA4FF810-74FC-4B3C-A65B-CFEE8A243EFA',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'X-Device-OS': 'iOS 14.0',
        'X-Device-Model-Name': 'Unknown Device',
        'Host': 'api.xueqiu.com',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close'
    }

    headers2 = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'cookie': 'Cookie: device_id=24700f9f1986800ab4fcc880530dd0ed; s=c215pkjwcq; bid=85974d5c8b844517db5e365540222743_kh5kmssc; cookiesu=231604734535085; snbim_minify=true; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1605320458,1605322825,1605322867,1605346376; remember=1; xq_a_token=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjA3MTgwMzE2LCJjdG0iOjE2MDUzNDYzOTMwNDcsImNpZCI6ImQ5ZDBuNEFadXAifQ.YGqAwdcSRYdtH6kOZ-aGjYK_h6RwhDK167sWLpos4gbkds-JOUGhTDJ17ZhRdf6j9GU59he38FFlYoWiw0GezPagP18XdtccS-bixFoViCgdJBmsde74WYN5F3C68ThvDYDlCMLuU1bomosbTmfPTU9q1sdHtYF5hBxsznEQiYKXiKqKF-_fg9PPw0uxSfvPFdgK2tEdrlMUl_t3xk4MS2s2ZBuyx3WjckQ68EwEoVzDIHbWNDksBFM9zlQaYseUDT7Iy6Y_n1liz_27i_TCXgKpBv3ZmHhxrr3Zcjm56vepMU0AxVaOuhnSE26yUZQpC1aU2xCsXwxPl5mABfzLuQ; xqat=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_r_token=352bedcf73f62ff28436ab06d1d490ff35be083f; xq_is_login=1; u=5007108385; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1605346391'
    }

    url = 'https://xueqiu.com/cubes/rank/arena_cubes.json?count='+ str(downloadcount) +'&cube_level='+ str(level) +'&list_param=list_overall&market=cn&page=1'


    response_data = requests.get(url, headers=headers)

    soup = bs4.BeautifulSoup(response_data.text, 'lxml')

    json_data = response_data.json()

    count = 0
    dict_d = dict(json_data).items()
    for k, v in dict_d:
        #print(k, ':', v)
        if k == 'list':
            for array_item in list(v):
                #print(array_item)
                count = 1 + count
                print('-------下载个数：-------' + str(count) + '------------------------')
                for stock_item_key, stock_item_value in dict(array_item).items():
                    # print(stock_item_key,':',stock_item_value)
                    if stock_item_key == 'symbol':
                        # print(str(dict(array_item).get('name')) + ":" + stock_item_value)
                        id = str(dict(array_item).get('id'))
                        name = str(dict(array_item).get('name'))
                        symbol = str(dict(array_item).get('symbol'))
                        owner_id = str(dict(array_item).get('owner_id'))
                        combination_tmp = Combination(id, name, symbol, owner_id)
                        my_list.append(combination_tmp)

                        # 创建文件夹

                        # output_dir = './output/' + str(count) + '_' + id + '_' + symbol + '_' + name + '/'
                        # isexists = os.path.exists(output_dir)
                        # if isexists:
                        #     print('文件夹已存在')
                        # else:
                        #     os.makedirs(output_dir)

                        # tmp_url = 'https://api.xueqiu.com/cubes/show.json?mix_rebalancing=true&ret_last_buy_rb_gid=true&symbol=ZH2128917&_=1605347420225&x=2.10004&_s=5ff080&_t=DA4FF810-74FC-4B3C-A65B-CFEE8A243EFA.9265171929.1605346596318.1605347250559'
                        tmp_url = 'https://api.xueqiu.com/cubes/show.json?_t=1NETEASEda8d1c2949d3ede8df407938af7c49da.5007108385.1604931242783.1604932210159&_s=a48f5d&ret_last_buy_rb_id=true&symbol=ZH2128917&mix_rebalancing=true'
                        x = requests.session()
                        # requests.utils.add_dict_to_cookiejar(x.cookies,{'cookie':'xq_a_token=ef60ae661da28e68f8918bc0e0d33ca59f30a148;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjkyNjUxNzE5MjksImlzcyI6InVjIiwiZXhwIjoxNjA3NTA1MjM2LCJjdG0iOjE2MDQ5MTMyMzY3NDUsImNpZCI6IldpQ2lteHBqNUgifQ.Jq_uKZsWUM1wIp-Nni6Q2WGs1zWguHMV9WDi7lejluE-KbsxdOJU5tpXUgRsbirlbLGdx0xZ7BdZdjLlxM_w2aXgVQ0h5H3IiW6vG82bzhSm4WSZN5qs7zZs7Dg5fvLRxdVtFbmNsMKjCfSSLtGjAikgUfIyn7SMUwQVQAadz4-8-386C28nbiY0fNp8eahLkbyBgBvBDiWnQryMX_d5Ka7a2xFgZYL0e1FjF0kdvC3NR10dTCl15J04yt4RYiroVWp4-1vyb_h5RIJXEYzv2plvePRAzvbYH8B_dIcaendBVzjy-5xDXjN2EkDASq2LfiNqw_MD01sxLnq5fSuAPA;u=9265171929'})
                        crruent_sto = x.get(tmp_url)
                        # crruent_sto = requests.get(tmp_url,headers)

                        # print(requests.sessions)
                        crruent_soup = bs4.BeautifulSoup(crruent_sto.text, 'lxml')
                        print(tmp_url)
                        print('------------------------ star get current soock ------------------------')
                        # print(crruent_soup)
                        time.sleep(sleeptime)
                        curret_stock = getResponse(symbol)
                        rb_id = tuple(curret_stock).__getitem__(0)
                        current_result = list(curret_stock).__getitem__(1)

                        list3 = []
                        current_result.sort(key=takesegment_id)
                        current_result.sort(key=takecruweight)
                        for i in current_result:
                            dict_tmp = i.__dict__
                            tmp_list = []
                            for k8, v8 in dict(dict_tmp).items():
                                tmp_list.append(v8)
                            list3.append(tmp_list)
                        time.sleep(sleeptime)
                        print('------------------------ star get last rebalance soock ------------------------')

                        list2 = []
                        rebalance_result = getRbResponse(rb_id)
                        rblist = list(rebalance_result)
                        rblist.sort(key=takerbsegment_id)
                        for i in rblist:
                            tmp_list = []
                            for k9, v9 in dict(i.__dict__).items():
                                tmp_list.append(v9)
                            list2.append(tmp_list)
                        if count == 1:
                            next_star_row = write_excel3(list3, list2, IsFirst=True, next_star_row=0, combinaname=name,
                                                         top=count,filename=filename)
                        else:
                            next_star_row = write_excel3(list3, list2, IsFirst=False, next_star_row=next_star_row,
                                                         combinaname=name, top=count,filename=filename)


# for i in my_list:
#     combination1 = i
#     combination1.myprint()


# import second


def tocvs():
    pass

def mktodaydir(output_dir=None):

    if os.path.exists(output_dir):
        print(output_dir + '文件夹已存在')
    else:
        os.makedirs(output_dir)

import shutil
def copyDir(target_path = None , source_path= None):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                print(src_file)

if __name__ == '__main__':

    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(':', '_').replace(' ','_')
    timeArray = time.localtime(int('1604293265928'[0:10]))  # 秒数
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(now_time)
    print(otherStyleTime)

    print(str(now_time) + ' 开始')
    print(str(now_time)[0:10] + ' 开始')
    #创建文件夹
    level_list = [(1,'近三个月.xls'),(2,'近六个月.xls'),(3,'近十二个月.xls')]

    mktodaydir(str(now_time))

    for i in level_list:
        pass
        print('level = '+ str(i[0]) + '开始时间为：' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(':', '_')))
        print(i)
        print(i[0])
        print(i[1])
        filename = str(now_time) + '/' + str(now_time)[0:10] + '_' + i[1]
        spider_xueqiu(level=i[0],filename = filename,downloadcount= 2 , sleeptime=10)
        print('level = ' + str(i[0]) + '结束时间为：' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(':', '_')))

    mktodaydir('/home/xueqiu/' + str(now_time))

    copyDir('/home/xueqiu/' + str(now_time),str(now_time))

    print(str(now_time) +  ' 已结束')