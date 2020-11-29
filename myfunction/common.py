import os
import pandas as pd
import datetime
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt, os


def castValuetoFloat(elem):
    if elem == None:
        return 0
    else:
        return elem



def castValuetoInt(elem):
    if elem == None:
        return 0
    else:
        return elem


def write_excel(data):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)

    for row in range(31):
        for col in range(len(data[0])):
            try:
                sheet.write(2 + row, 1 + col, data[row][col])
            except:
                print("nothing")
                pass

    for row in range(10):
        for col in range(len(data[0])):
            try:
                sheet.write(2 + row, 1 + 8 + col, data[row][col])
            except:
                print("nothing")
                pass

    xls.save('data.xls')


def write_excel2(current_data, rb_data, IsFirst=False, next_star_row=0, combinaname=None, top=1):
    if IsFirst:
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)
    else:
        rb = open_workbook('data6.xls')
        # rs  = rb.sheet_by_index(0)
        xls = copy(rb)
        sheet = xls.get_sheet(0)

    sheet.write(2 + next_star_row, 0, top)
    sheet.write(2 + next_star_row, 1, combinaname)

    max_value = max(len(current_data), len(rb_data))

    # 写表头和组合名称、组合排名
    current2 = [['stock_id', 'weight', 'segment_name', 'segment_id', 'stock_name', '更新时间', '', '调仓id', 'id',
                 'rebalancing_id', 'stock_id', 'stock_name', 'stock_symbol', 'volume', 'price', 'net_value', 'weight',
                 'target_weight', 'prev_weight', 'prev_target_weight', 'prev_weight_adjusted', 'prev_volume',
                 'prev_price', 'prev_net_value', 'proactive', 'created_at', 'updated_at', 'target_volume',
                 'prev_target_volume']]
    rb_data2 = []

    if IsFirst:
        for col in range(31):
            for row in range(1):
                try:
                    sheet.write(row + 1, col + 2, current2[row][col])
                except:
                    #print("nothing")
                    pass

    for row in range(next_star_row + max_value):
        for col in range(31):
            try:
                sheet.write(2 + next_star_row + row, 2 + col, current_data[row][col])
            except:
                #print("nothing")
                pass

    for row in range(next_star_row + max_value):
        for col in range(31):
            try:
                sheet.write(2 + next_star_row + row, 2 + 8 + col, rb_data[row][col])
            except:
                #print("nothing")
                pass

    next_star_row = max_value + next_star_row + 1

    xls.save('data6.xls')

    return next_star_row

def write_excel3(current_data, rb_data, IsFirst=False, next_star_row=0, combinaname=None, top=1,filename=None):
    if IsFirst:
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)
    else:
        rb = open_workbook(filename)
        # rs  = rb.sheet_by_index(0)
        xls = copy(rb)
        sheet = xls.get_sheet(0)

    sheet.write(2 + next_star_row, 0, top)
    sheet.write(2 + next_star_row, 1, combinaname)

    max_value = max(len(current_data), len(rb_data))

    # 写表头和组合名称、组合排名
    current2 = [['stock_id', 'weight', 'segment_name', 'segment_id', 'stock_name', '更新时间', '', '调仓id', 'id',
                 'rebalancing_id', 'stock_id', 'stock_name', 'rb_value', 'stock_symbol', 'volume', 'price', 'net_value', 'weight',
                 'target_weight', 'prev_weight', 'prev_target_weight', 'prev_weight_adjusted', 'prev_volume',
                 'prev_price', 'prev_net_value', 'proactive', 'created_at', 'updated_at', 'target_volume',
                 'prev_target_volume']]
    current2_chinese = [['股票ID', '占仓比例', '所属板块', '所属板块ID', '股票名称', '最新调整时间', '', '调仓id', '序列id',
                 '此次调仓ID', '股票ID', '股票名称', '调仓差值', '股票代号', '成交量', '成交价格', '净值', '调整后仓位值',
                 '目标仓位值', '先前仓位值', '先前目标仓位值', '先前仓位适应值', '先前成交量',
                 '先前成交价格', '先前净值', '积极or消极', '创建时间', '更新时间', '目标成交量',
                 '先前目标成交量']]

    if IsFirst:
        for col in range(32):
            #for row in range(0):
            row = 0
            try:
                sheet.write(row, col + 2 ,current2_chinese[row][col])
                sheet.write(row + 1, col + 2, current2[row][col])
            except:
                #print("nothing")
                pass

    for row in range(next_star_row + max_value):
        for col in range(32):
            try:
                sheet.write(2 + next_star_row + row, 2 + col, current_data[row][col])
            except:
                #print("nothing")
                pass

    for row in range(next_star_row + max_value):
        for col in range(32):
            try:
                sheet.write(2 + next_star_row + row, 2 + 8 + col, rb_data[row][col])
            except:
                #print("nothing")
                pass

    next_star_row = max_value + next_star_row + 1

    xls.save(filename)

    return next_star_row




if __name__ == '__main__':
    # isexists = os.path.exists('./ouput')
    # print(isexists)
    # os.makedirs('./output/' + str(isexists))
    #
    # df = pd.DataFrame([{'name':'APPLE','age':123}],columns=['name','age'])
    # df.to_csv('./output/' + str(isexists) + '/ooooo.csv', index=True)
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)

    data = [['name','age'],['a1','b1']]

    current = [['0','1000031','5.11','房地产','9850485','保利地产','1111'],
['1','1000920','7.43','有色金属','9764818','紫金矿业','1112'],
['2','1002155','4.88','电子','9833446','领益智造','1113'],
['3','1023025','1.5','电子','9833446','蓝思科技','1114'],
['4','1002031','4.35','电子','9833446','立讯精密','1115'],
['5','1002268','3.43','农林牧渔','9833447','牧原股份','1116'],
['6','1001909','2.56','机械设备','11011000','杰瑞股份','1117'],
['7','1001159','4.48','家用电器','9764820','美的集团','1118'],
['8','1000577','3.64','家用电器','9764820','海尔智家','1119'],
['9','1001087','5.11','房地产','9850485','万科A','1120'],
['10','1001891','1.1','电气设备','9764823','科华恒盛','1121'],
['11','1001329','2.07','传媒','9764819','视觉中国','1122'],
['12','1022825','3.42','传媒','9764819','芒果超媒','1123'],
['13','1002179','1.92','传媒','9764819','完美世界','1124'],
['14','1002149','3.72','汽车','9764821','比亚迪','1125'],
['15','1000928','1.98','银行','11011001','建设银行','1126'],
['16','1030646','3.86','电气设备','9764823','宁德时代','1127'],
['17','1000797','1.94','有色金属','9764818','赤峰黄金','1128'],
['18','1000895','1.95','非银金融','9850484','华泰证券','1129'],
['19','1000426','2.98','食品饮料','10090036','贵州茅台','1130'],
['20','1001274','2.02','有色金属','9764818','盛达资源','1131'],
['21','1003191','14','传媒','9764819','东方财富','1132'],
['22','1000170','2.01','农林牧渔','9833447','生物股份','1133'],
['23','1000349','5.25','化工','10932593','三友化工','1134'],
['24','1001306','3.08','家用电器','9764820','格力电器','1135'],
['25','1000483','4.13','建筑材料','9974143','海螺水泥','1136'],
['26','1001086','2.07','银行','11011001','平安银行','1137']]

    rb_data =[['0','233227264','82177254','1003146','亿纬锂能','SZ300014','0.00276645','48.8','0.135','9.42','9.42','10','10','9.42','0.00276645','49.35','0.1365243','TRUE','1.60022E+12','1.60022E+12','0.00276645','0.00276645'],
['1','233227265','82177254','1027160','恩捷股份','SZ002812','0.00181043','86.95','0.1574','10.98','10.98','10','10','10.98','0.00181043','75.41','0.13652452','TRUE','1.60022E+12','1.60022E+12','0.00181043','0.00181043'],
['2','233227266','82177254','1001607','三花智控','SZ002050','0.00653148','21.45','0.1401','9.78','9.78','10','10','9.73','0.00650117','21','0.13652457','TRUE','1.60022E+12','1.60022E+12','0.00653148','0.00650117'],
['3','233227267','82177254','1000758','宏发股份','SH600885','0.00294869','47.3','0.1395','9.73','9.73','10','10','9.73','0.00294869','46.3','0.13652434','TRUE','1.60022E+12','1.60022E+12','0.00294869','0.00294869'],
['4','233227268','82177254','1000626','华域汽车','SH600741','0.00554077','25.79','0.1429','9.97','9.97','10','10','9.97','0.00554077','24.64','0.13652457','TRUE','1.60022E+12','1.60022E+12','0.00554077','0.00554077'],
['5','233227269','82177254','1000084','上汽集团','SH600104','0.00748491','19.67','0.1472','10.27','10.27','10','10','10.27','0.00748491','18.24','0.13652475','TRUE','1.60022E+12','1.60022E+12','0.00748491','0.00748491'],
['6','233227270','82177254','1024487','先导智能','SZ300450','0.00292657','48.09','0.1407','9.82','9.82','10','10','9.82','0.00292657','46.65','0.13652449','TRUE','1.60022E+12','1.60022E+12','0.00292657','0.00292657'],
['7','233227271','82177254','1003255','汇川技术','SZ300124','0.00242279','53.79','0.1303','9.09','9.09','10','10','9.09','0.00242279','56.35','0.13652421','TRUE','1.60022E+12','1.60022E+12','0.00242279','0.00242279'],
['8','233227272','82177254','1030646','宁德时代','SZ300750','0.00073705','194.7','0.1435','10.01','10.01','10','10','10.01','0.00073705','185.23','0.13652377','TRUE','1.60022E+12','1.60022E+12','0.00073705','0.00073705'],
['9','233227273','82177254','1000550','福耀玻璃','SH600660','0.00488985','31.99','0.1564','10.92','10.92','10','10','10.92','0.00488985','27.92','0.13652461','TRUE','1.60022E+12','1.60022E+12','0.00488985','0.00488985'],
]

    #os.remove('data.xls')
    #write_excel(data)
    print(len(data))

    next_value = write_excel2(current , rb_data , IsFirst=True,next_star_row=0,combinaname='社会主义',top=1)

    next_value = write_excel2(current, rb_data, IsFirst=False, next_star_row=next_value,combinaname='社会主义2',top=2)
    print(range(1))



