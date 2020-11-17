import os
import pandas as pd
import datetime
if __name__ == '__main__':
    # isexists = os.path.exists('./ouput')
    # print(isexists)
    # os.makedirs('./output/' + str(isexists))
    #
    # df = pd.DataFrame([{'name':'APPLE','age':123}],columns=['name','age'])
    # df.to_csv('./output/' + str(isexists) + '/ooooo.csv', index=True)
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)

    import xlwt,os


    def write_excel(data):
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)

        for row in range(10):
            for col in range(len(data[0])):
                try:
                    sheet.write(1 + row, col, data[row][col])
                except:
                    print("nothing")
                    pass

        for row in range(10):
            for col in range(len(data[0])):
                try:
                    sheet.write(1 + len(data) + row, 10 + col, data[row][col])
                except:
                    print("nothing")
                    pass

        xls.save('data.xls')

    data = [['name','age'],['a1','b1']]
    os.remove('data.xls')
    write_excel(data)
    print(len(data))