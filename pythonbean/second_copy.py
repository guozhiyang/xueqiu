import bs4
import requests
import json,time
from pythonbean.combinationBean import Combination
from pythonbean.currentstockBean import currentstock
def getResponse(symbol):
    '将调用详细仓库，封装为方法'

    headers = {
        'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie':'xq_a_token=6dab2719a1fb6909d5af5ccd375fc906c06a43c4;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjkyNjUxNzE5MjksImlzcyI6InVjIiwiZXhwIjoxNjE0MjUzMTgzLCJjdG0iOjE2MTE2NjExODM1MzksImNpZCI6IldpQ2lteHBqNUgifQ.j6pSGZ-Shqk4I9mt2l9-qdiJvJWz20HidE02Ap1zdjgJ9BFBYseX7c7fBQJvNYqFtVtglIiSu2DTEkV7mSrLGkRi9vbB88aESKKm1S4EDdJ5A9VGnFclBExjHNH6G--47BETDWqvvzdeaN9B6TO-Ml35k6Ov-GojcXog5FCmnQWXLGaToaWN5L508qh-8rWDfbnx8oFGClEAQNMW7GZcHT-h0A2vA6FKKs-BZ2xh70po7uU8uAq3SZ3PcFsu57lu8vgptfGXopaTSwnK_xuB0vSYB6Z1B_SWz2_rkgyrUSmnwi9yuFdfThGCHktwLr_Em-NTdMEZMfP2GqLx1SKU8Q;u=9265171929'
    }

    url = 'https://api.xueqiu.com/cubes/show.json?_t=1NETEASEda8d1c2949d3ede8df407938af7c49da.5007108385.1604931242783.1604932210159&_s=a48f5d&ret_last_buy_rb_id=true&mix_rebalancing=true&symbol=' + symbol

    response_data = requests.get(url,headers=headers)

    soup = bs4.BeautifulSoup(response_data.text,'lxml')


    json_data = response_data.json()

    json_data_string = json.dumps(json_data)

    # json.JSONDecoder.decode(json_data_string)

    ss = json.loads(json_data_string)


    print('------------ 开始爬取：' + url + '-------------,返回值：' + str(json_data))

    currentstockList = []
    id = ''
    updated_at = ''
    dict_d = dict(json_data).items()
    for k,v in dict_d:

        if k == 'view_rebalancing':
            print(k, ':',v)
            for k2,v2 in dict(v).items():
                print(k2,":",v2)
                if k2 == 'id':
                    id = str(v2)
                if k2 == 'updated_at':
                    updated_at = str(v2)
                    timeArray = time.localtime(int(updated_at[0:10]))  # 秒数
                    updated_at_nyr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                if k2 == 'holdings':
                    for k3 in list(v2):
                        print(k3)
                        stock_id = str(dict(k3).get('stock_id'))
                        weight = str(dict(k3).get('weight'))
                        segment_name = str(dict(k3).get('segment_name'))
                        segment_id = str(dict(k3).get('segment_id'))
                        stock_name = str(dict(k3).get('stock_name'))
                        stock_symbol = str(dict(k3).get('stock_symbol'))
                        segment_color = str(dict(k3).get('segment_color'))
                        proactive = str(dict(k3).get('proactive'))
                        volume = str(dict(k3).get('volume'))
                        currentstock_tmp = currentstock(stock_id,weight,segment_name,segment_id,stock_name,updated_at_nyr)
                        currentstockList.append(currentstock_tmp)

    return id,currentstockList

def takesegment_id(elem):
    return elem.segment_id

if __name__ == '__main__':
    print(tuple(getResponse('ZH2128917')).__getitem__(0) + "--------------123")

    for i in  list(tuple(getResponse('ZH2128917')).__getitem__(1)):
        currentstock_tmp2 =  i
        currentstock_tmp2.myprint()
    print("1111111111111111111111111")
    list22 = list(tuple(getResponse('ZH2128917')).__getitem__(1))
    list22.sort(key=takesegment_id)
    for i in list22:
        i.myprint()