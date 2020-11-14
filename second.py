import bs4
import requests
import json
headers = {
    'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'cookie':'u=9265171929; xq_a_token=ef60ae661da28e68f8918bc0e0d33ca59f30a148; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjkyNjUxNzE5MjksImlzcyI6InVjIiwiZXhwIjoxNjA3NTA1MjM2LCJjdG0iOjE2MDQ5MTMyMzY3NDUsImNpZCI6IldpQ2lteHBqNUgifQ.Jq_uKZsWUM1wIp-Nni6Q2WGs1zWguHMV9WDi7lejluE-KbsxdOJU5tpXUgRsbirlbLGdx0xZ7BdZdjLlxM_w2aXgVQ0h5H3IiW6vG82bzhSm4WSZN5qs7zZs7Dg5fvLRxdVtFbmNsMKjCfSSLtGjAikgUfIyn7SMUwQVQAadz4-8-386C28nbiY0fNp8eahLkbyBgBvBDiWnQryMX_d5Ka7a2xFgZYL0e1FjF0kdvC3NR10dTCl15J04yt4RYiroVWp4-1vyb_h5RIJXEYzv2plvePRAzvbYH8B_dIcaendBVzjy-5xDXjN2EkDASq2LfiNqw_MD01sxLnq5fSuAPA; acw_tc=2760820e16053460746604045efe6a60a77a9ab89a082fd1b91668518d5930'
}

headers_pc = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'cookie':'device_id=24700f9f1986800ab4fcc880530dd0ed; s=c215pkjwcq; bid=85974d5c8b844517db5e365540222743_kh5kmssc; cookiesu=231604734535085; snbim_minify=true; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1605320458,1605322825,1605322867,1605346376; remember=1; xq_a_token=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjA3MTgwMzE2LCJjdG0iOjE2MDUzNDYzOTMwNDcsImNpZCI6ImQ5ZDBuNEFadXAifQ.YGqAwdcSRYdtH6kOZ-aGjYK_h6RwhDK167sWLpos4gbkds-JOUGhTDJ17ZhRdf6j9GU59he38FFlYoWiw0GezPagP18XdtccS-bixFoViCgdJBmsde74WYN5F3C68ThvDYDlCMLuU1bomosbTmfPTU9q1sdHtYF5hBxsznEQiYKXiKqKF-_fg9PPw0uxSfvPFdgK2tEdrlMUl_t3xk4MS2s2ZBuyx3WjckQ68EwEoVzDIHbWNDksBFM9zlQaYseUDT7Iy6Y_n1liz_27i_TCXgKpBv3ZmHhxrr3Zcjm56vepMU0AxVaOuhnSE26yUZQpC1aU2xCsXwxPl5mABfzLuQ; xqat=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_r_token=352bedcf73f62ff28436ab06d1d490ff35be083f; xq_is_login=1; u=5007108385; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1605346391'
}

url = 'https://api.xueqiu.com/cubes/show.json?_t=1NETEASEda8d1c2949d3ede8df407938af7c49da.5007108385.1604931242783.1604932210159&_s=a48f5d&ret_last_buy_rb_id=true&symbol=ZH2128917&mix_rebalancing=true'

response_data = requests.get(url,headers=headers)

soup = bs4.BeautifulSoup(response_data.text,'lxml')


json_data = response_data.json()

json_data_string = json.dumps(json_data)

# json.JSONDecoder.decode(json_data_string)

ss = json.loads(json_data_string)


dict_d = dict(json_data).items()
for k,v in dict_d:
    if k == 'view_rebalancing':
        print(k, ':',v)
        for k2,v2 in dict(v).items():
            print(k2,":",v2)
            if k2 == 'holdings':
                for k3 in list(v2):
                    print(k3)
