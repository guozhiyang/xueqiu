import bs4
import requests
import json,time
from pythonbean.combinationBean import Combination
from pythonbean.currentstockBean import currentstock
def getResponse(symbol):
    '将调用详细仓库，封装为方法'

    headers = {
        'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie':'device_id=24700f9f1986800ab4fcc880530dd0ed; s=c215pkjwcq; bid=85974d5c8b844517db5e365540222743_kh5kmssc; xq_a_token=ad26f3f7a7733dcd164fe15801383e62b6033003; xqat=ad26f3f7a7733dcd164fe15801383e62b6033003; xq_r_token=15b43888685621c645835bfe2d97242dc20b9005; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxMTI4MzA4NCwiY3RtIjoxNjEwMDA1NzE1OTQxLCJjaWQiOiJkOWQwbjRBWnVwIn0.Qtb2eiziDpDCDMJF2Mo1UxRbpyFuhI5O5yFgZSNr0tSLO3jcqXLaKvf_5Sx9BAlAPqxMlQ93cjDw05SSOozpV29liOw1ZN2uqbubJuT7T9Y9vqLu9tfHYu_IUgUs4qE12qqYCVhmtWunmy3zuz0iHQpYh5CmBvnlx_20aJpqhOhxMgultz1iUWjLpI7QTdzUXsHPGEhVgR2GVY-eIWNjDd-dWfTwNUEDt9mZO3cABfSPdetbSK2DRhUYV9JTX9V6ciwQIYh_dl6ZrCQC_V3bBnExAzwfr2iIcquUNIIi3MzwRAdSsLf9VhR7mtyTeQ-NZ_yd7fInXkp6B6rGMDbAoQ; u=471610005753132; Hm_lvt_1db88642e346389874251b5a1eded6e3=1610005752; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1610005764'
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