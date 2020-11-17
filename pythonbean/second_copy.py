import bs4
import requests
import json
from pythonbean.combinationBean import Combination
from pythonbean.currentstockBean import currentstock
def getResponse(symbol):
    '将调用详细仓库，封装为方法'

    headers = {
        'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie':'s=dh19xlxo1p; device_id=b7fe1386375035be0326473d9dd41da9; remember=1; xq_a_token=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjA3MTgwMzE2LCJjdG0iOjE2MDQ1ODgzMTYxODMsImNpZCI6ImQ5ZDBuNEFadXAifQ.TlJVttg2wZubRTYZMYA4IUSjX62pYRtnEuN0xJTUxmJrOTcSyR7hxKS0oY5q4GfwjwI_dxGbvqo0KtLcZGIWBRzwh8wc1SDcsFQfyZLpj7o15N2dLjYR23pV7nxZMXDWy6VLx_-juRLn9UNK28owjkHzT5U3dNwgmtNs158FBgQhz0QNxTdpfcU2pvnV87qPDYnskVIOxfQuqO2-f_25AcERo4Jy9Ht6nGpII6THUxQ-gJ0OfBAznPKmQzhusV4Yq9wpeLgblJ8VYvwg4uSn1ZtxkSOtzDRcg9F_OvjskVGtb8JOB7UAQg2VTKLLUwHeqKYZs67vRtM5JBwrKkjNmw; xqat=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_r_token=352bedcf73f62ff28436ab06d1d490ff35be083f; xq_is_login=1; u=5007108385; bid=85974d5c8b844517db5e365540222743_kh4ygcty; snbim_minify=true; _ga=GA1.2.1105802129.1604586313; _gid=GA1.2.103569105.1605095011; Hm_lvt_1db88642e346389874251b5a1eded6e3=1604586313,1604825947,1605094943,1605095055; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1605095100'
    }

    url = 'https://api.xueqiu.com/cubes/show.json?_t=1NETEASEda8d1c2949d3ede8df407938af7c49da.5007108385.1604931242783.1604932210159&_s=a48f5d&ret_last_buy_rb_id=true&mix_rebalancing=true&symbol=' + symbol

    response_data = requests.get(url,headers=headers)

    soup = bs4.BeautifulSoup(response_data.text,'lxml')


    json_data = response_data.json()

    json_data_string = json.dumps(json_data)

    # json.JSONDecoder.decode(json_data_string)

    ss = json.loads(json_data_string)

    currentstockList = []
    id = ''
    dict_d = dict(json_data).items()
    for k,v in dict_d:

        if k == 'view_rebalancing':
            print(k, ':',v)
            for k2,v2 in dict(v).items():
                print(k2,":",v2)
                if k2 == 'prev_bebalancing_id':
                    id = str(v2)
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
                        currentstock_tmp = currentstock(stock_id,weight,segment_name,segment_id,stock_name)
                        currentstockList.append(currentstock_tmp)

    return id,currentstockList
if __name__ == '__main__':
    print(tuple(getResponse('ZH2128917')).__getitem__(0) + "--------------123")
    for i in  list(tuple(getResponse('ZH2128917')).__getitem__(1)):
        currentstock_tmp2 =  i
        currentstock_tmp2.myprint()