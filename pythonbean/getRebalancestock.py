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
        'cookie':'device_id=24700f9f1986800ab4fcc880530dd0ed; s=c215pkjwcq; bid=85974d5c8b844517db5e365540222743_kh5kmssc; xq_a_token=ad26f3f7a7733dcd164fe15801383e62b6033003; xqat=ad26f3f7a7733dcd164fe15801383e62b6033003; xq_r_token=15b43888685621c645835bfe2d97242dc20b9005; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxMTI4MzA4NCwiY3RtIjoxNjEwMDA1NzE1OTQxLCJjaWQiOiJkOWQwbjRBWnVwIn0.Qtb2eiziDpDCDMJF2Mo1UxRbpyFuhI5O5yFgZSNr0tSLO3jcqXLaKvf_5Sx9BAlAPqxMlQ93cjDw05SSOozpV29liOw1ZN2uqbubJuT7T9Y9vqLu9tfHYu_IUgUs4qE12qqYCVhmtWunmy3zuz0iHQpYh5CmBvnlx_20aJpqhOhxMgultz1iUWjLpI7QTdzUXsHPGEhVgR2GVY-eIWNjDd-dWfTwNUEDt9mZO3cABfSPdetbSK2DRhUYV9JTX9V6ciwQIYh_dl6ZrCQC_V3bBnExAzwfr2iIcquUNIIi3MzwRAdSsLf9VhR7mtyTeQ-NZ_yd7fInXkp6B6rGMDbAoQ; u=471610005753132; Hm_lvt_1db88642e346389874251b5a1eded6e3=1610005752; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1610005764'
    }

    url = 'https://api.xueqiu.com/cubes/rebalancing/show_origin.json?rb_id=' + rb_id

    response_data = requests.get(url,headers=headers)

    soup = bs4.BeautifulSoup(response_data.text,'lxml')


    json_data = response_data.json()

    json_data_string = json.dumps(json_data)
    print('------------ 开始爬取：' + url + '-------------,返回值：' + str(json_data))
    ss = json.loads(json_data_string)

    rebalancestockList = []
    id = ''
    dict_d = dict(json_data).items()
    for k,v in dict_d:
        #print(k,v)
        if k == 'rebalancing':
            print(k, ':',v)
            if (str(dict(v).get('category')) == 'sys_rebalancing'):
                prev_rb_id = str(dict(v).get('prev_bebalancing_id'))
                print('这是一个系统分红时，产生的调仓ID。 当前ID=' + str(rb_id) + '此前ID为,PREV_RB_ID = ' + str(prev_rb_id) )
                return str(prev_rb_id)
            else:
                pass

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

    getRb_result = getRbResponse('83687797')

    while isinstance(getRb_result, str):
        getRb_result = getRbResponse(getRb_result)
    else:
        pass

    for i in list(getRb_result):
        i.myprint()
        print(i.__dict__)
        list2.append(i.__dict__)


    df = pd.DataFrame(list2,columns=['id','rebalancing_id','stock_id','stock_name','stock_symbol','volume','price','net_value','weight','target_weight','prev_weight','prev_target_weight','prev_weight_adjusted','prev_volume','prev_price','prev_net_value','proactive','created_at','updated_at','target_volume','prev_target_volume'])
    print(df)
    df.to_csv('./82177254.csv',index=True)
    pass
    #print(getRbResponse('82177254') + "--------------123")