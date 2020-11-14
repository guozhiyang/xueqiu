import pandas as pd


def test_pandas_read():
    for i in range(1, 6):
        sheet_name = "Sheet" + str(i)
        # df = pd.read_excel('test_cases\\read_xls.xls', sheet_name)
        df = pd.read_excel('test_cases\\read_xlsx.xlsx', sheet_name)

def test_pandas_write():
    df.to_excel(writer, 'Sheet1')
    df.to_excel(writer, 'Sheet2')
    df.to_excel(writer, 'Sheet3')
    df.to_excel(writer, 'Sheet4')
    df.to_excel(writer, 'Sheet5')
    writer.save()

import numpy as np

d = np.zeros([2000, 255])
d += 65536
df = pd.DataFrame(d)
# writer = pd.ExcelWriter('test_cases\\write_xls.xls')
writer = pd.ExcelWriter('write_xlsx.xlsx')
test_pandas_write()


