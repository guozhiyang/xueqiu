import bs4
import requests
import json,time
from pythonbean.combinationBean import Combination
from pythonbean.currentstockBean import currentstock
def getResponse(symbol):
    '将调用详细仓库，封装为方法'

    headers = {
        'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie':'s=dh19xlxo1p; device_id=b7fe1386375035be0326473d9dd41da9; bid=85974d5c8b844517db5e365540222743_kh4ygcty; _ga=GA1.2.1105802129.1604586313; Hm_lvt_1db88642e346389874251b5a1eded6e3=1604825947,1605094943,1605095055,1607260337; remember=1; xq_a_token=da85cf50f703a60e320894edb29b2c3c48cc1b24; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjA5ODUyNDU3LCJjdG0iOjE2MDcyNjA0NTc0NjgsImNpZCI6ImQ5ZDBuNEFadXAifQ.Jx9LJjDc2wOkaJtggJw-SHumN3mFgBcFgjyqWGT_8wadvTps9AH1uEpuiljQIPE6KD_Z-zBwMg-HN1OwUzn9FGVkoKQ756YYYtYyzcfIR-FzKWm0zkIPmLSlniTxJgunZR2K15lxpfJBP7IEwio8fszrgLnEP9iKhPzYyCHwMf-YOhPI-HnGUoZGcNxjJiWkQeRItgtam4F1DGVWKKiiqggshthv3kTh_pKBqwDJSeX3xcPemRRtb6nddXUK4QLzurTZWr0vnBoIri4aaXHL7m1V24pLlIiOqIC09wZTWasZMVUr89Kb5ekFi4SZrVCXSW2LF9TdPJqXTsTibcvvog; xqat=da85cf50f703a60e320894edb29b2c3c48cc1b24; xq_r_token=c17536456b0a92e3e330c8f13e8b0f89c22cc6ce; xq_is_login=1; u=5007108385; _gid=GA1.2.433169154.1607260465; snbim_minify=true; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1607261230'
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