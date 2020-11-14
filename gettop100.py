import sys
import time
import bs4
import requests

from pythonbean.combinationBean import Combination

sys.path.append('bean')
headers = {
    'User-agent':'Xueqiu iPhone 12.22',
    'cookie':'xq_a_token=ef60ae661da28e68f8918bc0e0d33ca59f30a148;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjkyNjUxNzE5MjksImlzcyI6InVjIiwiZXhwIjoxNjA3NTA1MjM2LCJjdG0iOjE2MDQ5MTMyMzY3NDUsImNpZCI6IldpQ2lteHBqNUgifQ.Jq_uKZsWUM1wIp-Nni6Q2WGs1zWguHMV9WDi7lejluE-KbsxdOJU5tpXUgRsbirlbLGdx0xZ7BdZdjLlxM_w2aXgVQ0h5H3IiW6vG82bzhSm4WSZN5qs7zZs7Dg5fvLRxdVtFbmNsMKjCfSSLtGjAikgUfIyn7SMUwQVQAadz4-8-386C28nbiY0fNp8eahLkbyBgBvBDiWnQryMX_d5Ka7a2xFgZYL0e1FjF0kdvC3NR10dTCl15J04yt4RYiroVWp4-1vyb_h5RIJXEYzv2plvePRAzvbYH8B_dIcaendBVzjy-5xDXjN2EkDASq2LfiNqw_MD01sxLnq5fSuAPA;u=9265171929',
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
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'cookie':'Cookie: device_id=24700f9f1986800ab4fcc880530dd0ed; s=c215pkjwcq; bid=85974d5c8b844517db5e365540222743_kh5kmssc; cookiesu=231604734535085; snbim_minify=true; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1605320458,1605322825,1605322867,1605346376; remember=1; xq_a_token=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjA3MTgwMzE2LCJjdG0iOjE2MDUzNDYzOTMwNDcsImNpZCI6ImQ5ZDBuNEFadXAifQ.YGqAwdcSRYdtH6kOZ-aGjYK_h6RwhDK167sWLpos4gbkds-JOUGhTDJ17ZhRdf6j9GU59he38FFlYoWiw0GezPagP18XdtccS-bixFoViCgdJBmsde74WYN5F3C68ThvDYDlCMLuU1bomosbTmfPTU9q1sdHtYF5hBxsznEQiYKXiKqKF-_fg9PPw0uxSfvPFdgK2tEdrlMUl_t3xk4MS2s2ZBuyx3WjckQ68EwEoVzDIHbWNDksBFM9zlQaYseUDT7Iy6Y_n1liz_27i_TCXgKpBv3ZmHhxrr3Zcjm56vepMU0AxVaOuhnSE26yUZQpC1aU2xCsXwxPl5mABfzLuQ; xqat=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_r_token=352bedcf73f62ff28436ab06d1d490ff35be083f; xq_is_login=1; u=5007108385; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1605346391'
}

url = 'https://xueqiu.com/cubes/rank/arena_cubes.json?count=1&cube_level=2&list_param=list_overall&market=cn&page=1'

url_current = 'https://api.xueqiu.com/cubes/rebalancing/show_origin.json?rb_id=84584981&ymbol='

response_data = requests.get(url,headers=headers)

soup = bs4.BeautifulSoup(response_data.text,'lxml')

print(soup)
json_data = response_data.json()
print(json_data)

count = 0

my_list = []

dict_d = dict(json_data).items()
for k,v in dict_d:
    print(k,':',v)
    if k == 'list':
        for array_item in list(v):
            print(array_item)
            count = 1+count
            print('--------------'+ str(count) +'------------------------')
            for stock_item_key,stock_item_value in dict(array_item).items():
                #print(stock_item_key,':',stock_item_value)
                if stock_item_key == 'symbol':
                    print(str(dict(array_item).get('name')) + ":" + stock_item_value)
                    id = str(dict(array_item).get('id'))
                    name = str(dict(array_item).get('name'))
                    symbol = str(dict(array_item).get('symbol'))
                    owner_id = str(dict(array_item).get('owner_id'))
                    combination_tmp = Combination(id,name,symbol,owner_id)
                    my_list.append(combination_tmp)



                    tmp_url = 'https://api.xueqiu.com/cubes/show.json?mix_rebalancing=true&ret_last_buy_rb_gid=true&symbol=ZH2128917&_=1605347420225&x=2.10004&_s=5ff080&_t=DA4FF810-74FC-4B3C-A65B-CFEE8A243EFA.9265171929.1605346596318.1605347250559'
                    x = requests.session()
                    # requests.utils.add_dict_to_cookiejar(x.cookies,{'cookie':'xq_a_token=ef60ae661da28e68f8918bc0e0d33ca59f30a148;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjkyNjUxNzE5MjksImlzcyI6InVjIiwiZXhwIjoxNjA3NTA1MjM2LCJjdG0iOjE2MDQ5MTMyMzY3NDUsImNpZCI6IldpQ2lteHBqNUgifQ.Jq_uKZsWUM1wIp-Nni6Q2WGs1zWguHMV9WDi7lejluE-KbsxdOJU5tpXUgRsbirlbLGdx0xZ7BdZdjLlxM_w2aXgVQ0h5H3IiW6vG82bzhSm4WSZN5qs7zZs7Dg5fvLRxdVtFbmNsMKjCfSSLtGjAikgUfIyn7SMUwQVQAadz4-8-386C28nbiY0fNp8eahLkbyBgBvBDiWnQryMX_d5Ka7a2xFgZYL0e1FjF0kdvC3NR10dTCl15J04yt4RYiroVWp4-1vyb_h5RIJXEYzv2plvePRAzvbYH8B_dIcaendBVzjy-5xDXjN2EkDASq2LfiNqw_MD01sxLnq5fSuAPA;u=9265171929'})
                    # crruent_sto = x.get(tmp_url)
                    crruent_sto = requests.get(tmp_url,headers)

                    print(requests.sessions)
                    crruent_soup = bs4.BeautifulSoup(crruent_sto.text,'lxml')
                    print(tmp_url)
                    print('111111111111111111111111111111111111111111111111')
                    print(crruent_soup)

for i in my_list:
    combination1 = i
    combination1.myprint()
