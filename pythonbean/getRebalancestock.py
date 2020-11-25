import bs4
import requests
import json,time
from pythonbean.combinationBean import Combination
from pythonbean.rebalancestockBean import rebalancestock
from myfunction.common import castValuetoFloat

def getRbResponse(rb_id):
    '将调用详细仓库，封装为方法'

    headers = {
        'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'cookie':'s=dh19xlxo1p; device_id=b7fe1386375035be0326473d9dd41da9; remember=1; xq_a_token=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjA3MTgwMzE2LCJjdG0iOjE2MDQ1ODgzMTYxODMsImNpZCI6ImQ5ZDBuNEFadXAifQ.TlJVttg2wZubRTYZMYA4IUSjX62pYRtnEuN0xJTUxmJrOTcSyR7hxKS0oY5q4GfwjwI_dxGbvqo0KtLcZGIWBRzwh8wc1SDcsFQfyZLpj7o15N2dLjYR23pV7nxZMXDWy6VLx_-juRLn9UNK28owjkHzT5U3dNwgmtNs158FBgQhz0QNxTdpfcU2pvnV87qPDYnskVIOxfQuqO2-f_25AcERo4Jy9Ht6nGpII6THUxQ-gJ0OfBAznPKmQzhusV4Yq9wpeLgblJ8VYvwg4uSn1ZtxkSOtzDRcg9F_OvjskVGtb8JOB7UAQg2VTKLLUwHeqKYZs67vRtM5JBwrKkjNmw; xqat=bbd3d0975ab8044b5393c071c927f68f46b0efe3; xq_r_token=352bedcf73f62ff28436ab06d1d490ff35be083f; xq_is_login=1; u=5007108385; bid=85974d5c8b844517db5e365540222743_kh4ygcty; snbim_minify=true; _ga=GA1.2.1105802129.1604586313; _gid=GA1.2.103569105.1605095011; Hm_lvt_1db88642e346389874251b5a1eded6e3=1604586313,1604825947,1605094943,1605095055; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1605095100'
    }

    url = 'https://api.xueqiu.com/cubes/rebalancing/show_origin.json?rb_id=' + rb_id

    response_data = requests.get(url,headers=headers)

    soup = bs4.BeautifulSoup(response_data.text,'lxml')


    json_data = response_data.json()

    json_data_string = json.dumps(json_data)

    ss = json.loads(json_data_string)

    rebalancestockList = []
    id = ''
    dict_d = dict(json_data).items()
    for k,v in dict_d:
        #print(k,v)
        if k == 'rebalancing':
            print(k, ':',v)
            for k2,v2 in dict(v).items():
                if k2 == 'rebalancing_histories':
                    for k3 in list(v2):
                        print(k3)
                        id = str(castValuetoFloat(dict(k3).get('id')))
                        stock_id = str(castValuetoFloat(dict(k3).get('stock_id')))
                        stock_name = str(castValuetoFloat(dict(k3).get('stock_name')))
                        stock_symbol = str(castValuetoFloat(dict(k3).get('stock_symbol')))
                        volume = str(castValuetoFloat(dict(k3).get('volume')))
                        price = str(castValuetoFloat(dict(k3).get('price')))
                        net_value = str(castValuetoFloat(dict(k3).get('net_value')))
                        weight = str(castValuetoFloat(dict(k3).get('weight')))
                        target_weight = str(castValuetoFloat(dict(k3).get('target_weight')))
                        prev_weight = str(castValuetoFloat(dict(k3).get('prev_weight')))
                        prev_target_weight = str(castValuetoFloat(dict(k3).get('prev_target_weight')))
                        prev_weight_adjusted = str(castValuetoFloat(dict(k3).get('prev_weight_adjusted')))
                        prev_volume = str(castValuetoFloat(dict(k3).get('prev_volume')))
                        prev_price = str(castValuetoFloat(dict(k3).get('prev_price')))
                        prev_net_value = str(castValuetoFloat(dict(k3).get('prev_net_value')))
                        proactive = str(castValuetoFloat(dict(k3).get('proactive')))
                        created_at = str(castValuetoFloat(dict(k3).get('created_at')))
                        updated_at = str(castValuetoFloat(dict(k3).get('updated_at')))
                        target_volume = str(castValuetoFloat(dict(k3).get('target_volume')))
                        prev_target_volume = str(castValuetoFloat(dict(k3).get('prev_target_volume')))

                        rb_value = str(round(float(float(weight) - float(prev_weight_adjusted)),2))

                        print('计算调整值为：' + rb_value)

                        timeArray = time.localtime(int(updated_at[0:10]))  # 秒数
                        updated_at_nyr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

                        timeArray2 = time.localtime(int(created_at[0:10]))  # 秒数
                        created_at_nyr = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)

                        rebalancestock_tmp = rebalancestock(id,str(rb_id),stock_id,stock_name,rb_value,stock_symbol,volume,price,net_value,weight,target_weight,prev_weight,prev_target_weight,prev_weight_adjusted,prev_volume,prev_price,prev_net_value,proactive,created_at_nyr,updated_at_nyr,target_volume,prev_target_volume)
                        rebalancestockList.append(rebalancestock_tmp)

    return rebalancestockList

import pandas as pd
if __name__ == '__main__':
    list2 = []
    for i in list(getRbResponse('82177254')):
        i.myprint()
        print(i.__dict__)
        list2.append(i.__dict__)


    df = pd.DataFrame(list2,columns=['id','rebalancing_id','stock_id','stock_name','stock_symbol','volume','price','net_value','weight','target_weight','prev_weight','prev_target_weight','prev_weight_adjusted','prev_volume','prev_price','prev_net_value','proactive','created_at','updated_at','target_volume','prev_target_volume'])
    print(df)
    df.to_csv('./82177254.csv',index=True)
    pass
    #print(getRbResponse('82177254') + "--------------123")